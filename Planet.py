from math import *


class Planet:

    def __init__(self, sheet, x, y, radius, color, speed_x, speed_y, weight):
        self.sheet = sheet
        self.radius = radius
        self.position_x = x
        self.position_y = y
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.weight = weight

    def set_speed_x(self, v_x):
        self.speed_x = v_x

    def set_speed_y(self, v_y):
        self.speed_y = v_y

    def set_position_x(self, x):
        self.position_x = x

    def set_position_y(self, y):
        self.position_y = y
