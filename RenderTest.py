# Thomas Safago
# 04/13/2024


from Game import Game
from Pixel import Pixel
from RenderLayer import RenderLayer
from RenderQueue import RenderQueue

import math
import keyboard


class RenderTest(Game):
    # Attributes
    __x_off = 0
    __y_off = 0

    # Init
    def __init__(self):
        super().__init__()

    # Methods
    def next(self, dtime):
        if keyboard.is_pressed("a"):
            self.__x_off -= dtime * 2
        if keyboard.is_pressed("d"):
            self.__x_off += dtime * 2
        if keyboard.is_pressed("w"):
            self.__y_off -= dtime * 4
        if keyboard.is_pressed("s"):
            self.__y_off += dtime * 4

        if keyboard.is_pressed("q"):
            return "GameSelector"

    def render(self, x, y):
        l1 = RenderLayer(x, y)

        eps = 0.6

        for nx in range(l1.get_x()):
            for ny in range(l1.get_y()):
                if -eps < 10*math.sin(nx*math.pi/50 + self.__x_off)+ny - 20 + self.__y_off < eps:
                    l1.set_pixel(nx, ny, Pixel('0'))

        return l1

    # Getters

    # Setters

    # To string
    def __str__(self):
        pass

