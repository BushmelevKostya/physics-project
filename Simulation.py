import pygame
import yaml
from pygame import *

from FlyObjBox import FlyObjBox
from Planet import Planet


class Simulation:
    FLAG = True
    timer = pygame.time.Clock()

    def start(self):
        params = self.get_params()

        # window parameters
        width = params["display"]["width"]
        height = params["display"]["height"]
        space_color = params["display"]["color"]
        main_display = (width, height)
        screen = pygame.display.set_mode(main_display)
        sheet = Surface(main_display)

        count_planets = params["count"]
        planets = []

        for num_planet in range(count_planets):
            name_planet = self.get_name_planet(num_planet)
            pos_x = width / 2 if name_planet == "sun" else params[name_planet]["x"]
            pos_y = height / 2 if name_planet == "sun" else params[name_planet]["y"]
            if name_planet != "sun":
                width = params[name_planet]["width"]
                height = params[name_planet]["height"]
            radius = params[name_planet]["radius"]
            col = params[name_planet]["color"]
            speed_x = params[name_planet]["speed_x"]
            speed_y = params[name_planet]["speed_y"]
            weight = params[name_planet]["weight"]
            planet_sheet = Surface((width, height))
            planets.append(Planet(planet_sheet, pos_x, pos_y, radius, col, speed_x, speed_y, weight))

        self.initialize(planets, sheet, space_color, width, height)

        dt = params["dt"]
        fly_obj_box = FlyObjBox()
        while self.FLAG:
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.FLAG = False
                    break

            x = [0] * len(planets)
            y = [0] * len(planets)

            fly_obj_box.set_planets(planets)
            for i in range(0, count_planets):
                a_x, a_y = fly_obj_box.calc_acceleration(i, count_planets)
                v_x, v_y = fly_obj_box.calc_speed(i, a_x, a_y, dt)
                x[i], y[i] = fly_obj_box.calc_position(i, v_x, v_y, dt)

                planets[i].set_speed_x(v_x)
                planets[i].set_speed_y(v_y)
                planets[i].set_position_x(x[i])
                planets[i].set_position_y(y[i])

                fly_obj_box.f_x = 0
                fly_obj_box.f_y = 0

            fly_obj_box.reset()

            screen.blit(sheet, (0, 0))
            for planet in planets:
                screen.blit(planet.sheet, (planet.position_x, planet.position_y))
            pygame.display.update()

    def initialize(self, planets, sheet, space_color, width, height):
        pygame.init()
        pygame.display.set_caption("Simulation of gravitational interaction")

        sheet.fill(Color(space_color))

        for planet in planets[1:]:
            self.__draw_planet(planet, width, height)

        self.__draw_planet(planets[0], 0, 0)
        self.__draw_sun(sheet, planets[0])

    @staticmethod
    def get_params():
        file_path = "config.yml"
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)

        return data

    @staticmethod
    def get_name_planet(num):
        if num == 0:
            return "sun"
        elif num == 1:
            return "comet"
        return "planet-" + str(num - 1)

    @staticmethod
    def __draw_sun(sheet, sun):
        draw.circle(sheet, Color(sun.color), (sun.position_x, sun.position_y), sun.radius)

    @staticmethod
    def __draw_planet(planet, width, height):
        draw.circle(planet.sheet, Color(planet.color), (width // 2, height // 2), planet.radius)
        planet.sheet.set_colorkey((0, 0, 0, 0))
