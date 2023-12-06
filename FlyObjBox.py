from math import *


class FlyObjBox:

    planets = []
    f_x = 0
    f_y = 0

    G = 6.674 * 10**-11

    def add_planet(self, planet):
        self.planets.append(planet)

    def set_planets(self, planets):
        self.planets = planets

    def calc_acceleration(self, i, count_planets):
        for j in range(0, count_planets):
            if i != j:
                r = sqrt((self.planets[j].position_x - self.planets[i].position_x) ** 2 +
                         (self.planets[j].position_y - self.planets[i].position_y) ** 2) * 1.392e8 / sqrt(10)
                F = self.G * self.planets[i].weight * self.planets[j].weight / r ** 2
                ##
                print("distance: ", r)
                print("first x: ", self.planets[j].position_x, "y: ", self.planets[j].position_y)
                print("second x: ", self.planets[i].position_x, "y: ", self.planets[i].position_y)
                print("F: ", F)
                # exit(-1)

                ##
                cosine = 1.392e8 / sqrt(10) * (self.planets[j].position_x - self.planets[i].position_x) / r
                sinus = 1.392e8 / sqrt(10) * (self.planets[j].position_y - self.planets[i].position_y) / r
                F_x = F * cosine
                F_y = F * sinus
                self.f_x += F_x
                self.f_y += F_y
        a_x = self.f_x / self.planets[i].weight
        a_y = self.f_y / self.planets[i].weight
        print("body a_y: ", a_y, "a_x: ", a_x)
        return a_x, a_y

    def calc_speed(self, i, a_x, a_y, dt):
        v_x = self.planets[i].speed_x + a_x * dt
        v_y = self.planets[i].speed_y + a_y * dt
        return v_x, v_y

    def calc_position(self, i, v_x, v_y, dt):
        x = self.planets[i].position_x + v_x * dt
        y = self.planets[i].position_y + v_y * dt
        return x, y

    def reset(self):
        self.planets = []
