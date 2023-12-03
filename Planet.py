from math import *
class Planet:
    acceleration_x = 0.0
    acceleration_y = 0.0

    def __init__(self, x, y, radius, color, distance, speed_x, speed_y):
        self.radius = radius
        self.position_x = x
        self.position_y = y
        self.color = color
        self.distance_to_sun = distance
        self.speed_x = speed_x
        self.speed_y = speed_y

    def set_distance_to_sun(self, sun_x, sun_y):
        self.distance_to_sun = sqrt((self.position_x - sun_x) ** 2 + (self.position_y - sun_y) ** 2)
        return self.distance_to_sun

    def set_acceleration_x(self, sun_weight, sun_x):
        self.acceleration_x = sun_weight * (sun_x - self.position_x) / self.distance_to_sun ** 3
        return self.acceleration_x
    
    def set_acceleration_y(self, sun_weight, sun_y):
        self.acceleration_y = sun_weight * (sun_y - self.position_y) / self.distance_to_sun ** 3
        return self.acceleration_y
    
    def set_speed_x(self):
        self.speed_x += self.acceleration_x
        return self.speed_x
    
    def set_speed_y(self):
        self.speed_y += self.acceleration_y
        return self.speed_y

    def set_position_x(self):
        self.position_x += self.speed_x
        return self.position_x

    def set_position_y(self):
        self.position_y += self.speed_y
        return self.position_y
