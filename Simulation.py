import pygame
from pygame import *

from Planet import Planet
from Sun import Sun


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

    def start(self):
        screen = pygame.display.set_mode(self.DISPLAY)
        sheet = Surface(self.DISPLAY)
        # to config
        sun_radius = 10
        # to config
        weight = 5000
        sun = Sun(self.CENTER_X, self.CENTER_Y, sun_radius, weight)

        # to config
        planet_radius = 5
        # to config
        position_planet_x = 100
        # to config
        position_planet_y = 290
        # to config
        distance_to_sun = 0.0
        # to config
        speed_x = 0.1
        # to config
        speed_y = 1.5

        planet_sheet = Surface((self.PLANET_WIDTH, self.PLANET_HEIGHT))
        planet = Planet(position_planet_x, position_planet_y, planet_radius, "green", distance_to_sun, speed_x, speed_y)

        self.initialize(sun, planet, planet_sheet, screen, sheet)
        while self.FLAG:
            self.timer.tick(50)
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.FLAG = False
                    break

            planet.set_distance_to_sun(sun.position_x, sun.position_y)
            planet.set_acceleration_x(sun.weight, sun.position_x)
            planet.set_acceleration_y(sun.weight, sun.position_y)
            planet.set_speed_x()
            planet.set_speed_y()
            planet_x = planet.set_position_x()
            planet_y = planet.set_position_y()

            screen.blit(sheet, (0, 0))
            screen.blit(planet_sheet, (planet_x, planet_y))
            pygame.display.update()

    def initialize(self, sun, planet, planet_sheet, screen, sheet):
        pygame.init()
        pygame.display.set_caption("Simulation of gravitational interaction")

        sheet.fill(Color(self.SPACE_COLOR))

        self.__drawSun(sheet, sun)
        self.__drawPlanet(planet_sheet, planet)

    def __drawSun(self, sheet, sun):
        draw.circle(sheet, Color(sun.color), (sun.position_x, sun.position_y), sun.radius)

    def __drawPlanet(self, planet_sheet, planet):
        planet_sheet.fill(Color(self.SPACE_COLOR))
        draw.circle(planet_sheet, Color(planet.color), (self.PLANET_WIDTH // 2, self.PLANET_HEIGHT // 2), planet.radius)
