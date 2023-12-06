from math import *


class FlyObjBox:
    m = []
    v_x = []
    v_y = []
    x = []
    y = []
    f_x = 0
    f_y = 0
    # change this constant (until = 1)
    G = 6.674 * 10**-11
    # G = 1

    def addPlanet(self, planet):
        self.v_x.append(planet.speed_x)
        self.v_y.append(planet.speed_y)
        self.x.append(planet.position_x)
        self.y.append(planet.position_y)
        self.m.append(planet.weight)

    def calcAcceleration(self, i, N):
        scale = 8.9 / 12 * (10 ** 8)
        print(scale, 1.392e8 / sqrt(10))
        for j in range(0, N):
            if i != j:
                r = sqrt((self.x[j] - self.x[i]) ** 2 + (self.y[j] - self.y[i]) ** 2) * scale
                F = self.G * self.m[i] * self.m[j] / r ** 2
                ##
                print("distance: ", r)
                print("first x: ", self.x[j], "y: ", self.y[j])
                print("second x: ", self.x[i], "y: ", self.y[i])
                print("F: ", F)
                # exit(-1)

                ##
                cosine = scale * (self.x[j] - self.x[i]) / r
                sinus = scale * (self.y[j] - self.y[i]) / r
                F_x = F * cosine
                F_y = F * sinus
                self.f_x += F_x
                self.f_y += F_y
        a_x = self.f_x / self.m[i]
        a_y = self.f_y / self.m[i]
        print("body a_y: ", a_y, "a_x: ", a_x)
        return a_x, a_y

    def calcSpeed(self, i, a_x, a_y, dt):
        v_x = self.v_x[i] + a_x * dt
        v_y = self.v_y[i] + a_y * dt
        return v_x, v_y

    def calcPosition(self, i, v_x, v_y, dt):
        x = self.x[i] + v_x * dt
        y = self.y[i] + v_y * dt
        return x, y

    def reset(self):
        self.m = []
        self.v_x = []
        self.v_y = []
        self.x = []
        self.y = []
