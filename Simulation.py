import pygame
import yaml
from pygame import *

from FlyObjBox import FlyObjBox
from Planet import Planet


class Simulation:
    FLAG = True
    timer = pygame.time.Clock()

    def start(self):
        params = self.getParams()

        width = params["display"]["width"]
        height = params["display"]["height"]
        main_display = (width, height)
        screen = pygame.display.set_mode(main_display)

        sheet = Surface(main_display)

        center_x = width / 2
        center_y = height / 2
        radius = params["sun"]["radius"]
        col = params["sun"]["color"]
        speed_x = params["sun"]["speed_x"]
        speed_y = params["sun"]["speed_y"]
        weight = params["sun"]["weight"]

        sun = Planet(center_x, center_y, radius, col, speed_x, speed_y, weight)

        width = params["planet-1"]["width"]
        height = params["planet-1"]["height"]
        radius = params["planet-1"]["radius"]
        col = params["planet-1"]["color"]
        x = params["planet-1"]["x"]
        y = params["planet-1"]["y"]
        speed_x = params["planet-1"]["speed_x"]
        speed_y = params["planet-1"]["speed_y"]
        weight = params["planet-1"]["weight"]

        planet_sheet = Surface((width, height))
        planet = Planet(x, y, radius, col, speed_x, speed_y, weight)

        width = params["comet"]["width"]
        height = params["comet"]["height"]
        radius = params["comet"]["radius"]
        col = params["comet"]["color"]
        x = params["comet"]["x"]
        y = params["comet"]["y"]
        speed_x = params["comet"]["speed_x"]
        speed_y = params["comet"]["speed_y"]
        weight = params["comet"]["weight"]

        comet_sheet = Surface((width, height))
        comet = Planet(x, y, radius, col, speed_x, speed_y, weight)

        space_color = params["display"]["color"]
        self.initialize(sun, planet, planet_sheet, comet, comet_sheet, sheet, space_color, width, height)

        N = params["count"]
        planets = [planet, comet, sun]
        dt = params["dt"]
        fly_obj_box = FlyObjBox()
        while self.FLAG:
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.FLAG = False
                    break

            x = [0, 0]
            y = [0, 0]

            fly_obj_box.add_planet(planets[0])
            fly_obj_box.add_planet(planets[1])
            fly_obj_box.add_planet(planets[2])
            for i in range(0, N - 1):
                a_x, a_y = fly_obj_box.calc_acceleration(i, N)
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
            screen.blit(planet_sheet, (planets[0].position_x, planets[0].position_y))
            screen.blit(comet_sheet, (planets[1].position_x, planets[1].position_y))
            pygame.display.update()

    def getParams(self):
        file_path = "config.yml"
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)

        return data

    def initialize(self, sun, planet, planet_sheet, comet, comet_sheet, sheet, space_color, width, height):
        pygame.init()
        pygame.display.set_caption("Simulation of gravitational interaction")

        sheet.fill(Color(space_color))

        self.__drawSun(sheet, sun)
        self.__drawPlanet(planet_sheet, planet, space_color, width, height)
        self.__drawPlanet(comet_sheet, comet, space_color, width, height)

    def __drawSun(self, sheet, sun):
        draw.circle(sheet, Color(sun.color), (sun.position_x, sun.position_y), sun.radius)

    def __drawPlanet(self, planet_sheet, planet, space_color, width, height):
        draw.circle(planet_sheet, Color(planet.color), (width // 2, height // 2), planet.radius)
        planet_sheet.set_colorkey((0, 0, 0, 0))
