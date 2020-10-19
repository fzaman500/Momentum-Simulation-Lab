import random
import matplotlib.pyplot as plt
import time
import numpy as np


class Object:
    def __init__(self, speed_x=0.0, speed_y=0.0, mass=0.0):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.mass = mass

class System:
    def __init__(self, obj1, obj2, elastic=True):
        self.obj1 = obj1
        self.obj2 = obj2
        self.elastic = elastic

    def elastic_collision(self):
        vcm_x = (self.obj1.mass * self.obj1.speed_x + self.obj2.mass * self.obj2.speed_x) / (self.obj1.mass + self.obj2.mass)
        v1f_x = 2*vcm_x - self.obj1.speed_x
        v2f_x = 2 * vcm_x - self.obj2.speed_x
        vcm_y = (self.obj1.mass * self.obj1.speed_y + self.obj2.mass * self.obj2.speed_y) / (
                    self.obj1.mass + self.obj2.mass)
        v1f_y = 2 * vcm_y - self.obj1.speed_y
        v2f_y = 2 * vcm_x - self.obj2.speed_y
        return v1f_x, v2f_x, v1f_y, v2f_y

    def inelastic_collision(self):
        final_vx = (self.obj1.speed_x * self.obj1.mass + self.obj2.speed_x * self.obj2.mass) / (self.obj1.mass + self.obj2.mass)
        final_vy = (self.obj1.speed_y * self.obj1.mass + self.obj2.speed_y * self.obj2.mass) / (self.obj1.mass + self.obj2.mass)
        return final_vx, final_vy


if __name__ == '__main__':
    elasticity = bool(input("Elastic? (True/False)"))
    obj1 = list(map(float, input().split()))
    obj1 = Object(speed_x=obj1[0], speed_y=obj1[1], mass=obj1[2])
    obj2 = list(map(float, input().split()))
    obj2 = Object(speed_x=obj2[0], speed_y=obj2[1], mass=obj2[2])
    System(obj1, obj2, elastic=elasticity)