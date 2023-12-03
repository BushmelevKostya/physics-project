import time

import pygame
from pygame import *

from FlyObjBox import FlyObjBox
from Planet import Planet


class Simulation:
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 640
    PLANET_WIDTH = 20
    PLANET_HEIGHT = 20
    CENTER_X = WINDOW_WIDTH / 2
    CENTER_Y = WINDOW_HEIGHT / 2
    DISPLAY = (WINDOW_WIDTH, WINDOW_HEIGHT)
    SPACE_COLOR = "#000022"
    FLAG = True
    timer = pygame.time.Clock()
    N = 3

    def start(self):
        screen = pygame.display.set_mode(self.DISPLAY)
        sheet = Surface(self.DISPLAY)
        # to config
        sun_radius = 10
        # to config
        weight = 50
        sun = Planet(self.CENTER_X, self.CENTER_Y, sun_radius, "yellow", 0, 0, weight)

        # to config
        planet_radius = 5
        # to config
        position_planet_x = 100
        # to config
        position_planet_y = 290
        # to config
        weight = 2
        # to config
        speed_x = 0.1
        # to config
        speed_y = 0.15

        planet_sheet = Surface((self.PLANET_WIDTH, self.PLANET_HEIGHT))
        planet = Planet(position_planet_x, position_planet_y, planet_radius, "green", speed_x, speed_y, weight)

        # to config
        comet_radius = 3
        # to config
        position_comet_x = 200
        # to config
        position_comet_y = 290
        # to config
        weight = 1
        # to config
        speed_x = 0.2
        # to config
        speed_y = 0.4

        comet_sheet = Surface((self.PLANET_WIDTH, self.PLANET_HEIGHT))
        comet = Planet(position_comet_x, position_comet_y, comet_radius, "red", speed_x, speed_y, weight)

        self.initialize(sun, planet, planet_sheet, comet, comet_sheet, screen, sheet)

        planets = [planet, comet, sun]
        dt = 0.5
        fly_obj_box = FlyObjBox()
        while self.FLAG:
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.FLAG = False
                    break

            x = [0, 0]
            y = [0, 0]

            fly_obj_box.addPlanet(planets[0])
            fly_obj_box.addPlanet(planets[1])
            fly_obj_box.addPlanet(planets[2])
            for i in range(0, self.N - 1):
                a_x, a_y = fly_obj_box.calcAcceleration(i, self.N)
                v_x, v_y = fly_obj_box.calcSpeed(i, a_x, a_y, dt)
                x[i], y[i] = fly_obj_box.calcPosition(i, v_x, v_y, dt)

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


    def initialize(self, sun, planet, planet_sheet, comet, comet_sheet, screen, sheet):
        pygame.init()
        pygame.display.set_caption("Simulation of gravitational interaction")

        sheet.fill(Color(self.SPACE_COLOR))

        self.__drawSun(sheet, sun)
        self.__drawPlanet(planet_sheet, planet)
        self.__drawPlanet(comet_sheet, comet)

    def __drawSun(self, sheet, sun):
        draw.circle(sheet, Color(sun.color), (sun.position_x, sun.position_y), sun.radius)

    def __drawPlanet(self, planet_sheet, planet):
        planet_sheet.fill(Color(self.SPACE_COLOR))
        draw.circle(planet_sheet, Color(planet.color), (self.PLANET_WIDTH // 2, self.PLANET_HEIGHT // 2), planet.radius)
