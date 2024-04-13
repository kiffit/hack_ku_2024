# Thomas Safago
# 04/13/2024


from Game import Game
from Pixel import Pixel
from RenderLayer import RenderLayer
from RenderQueue import RenderQueue


import math
import keyboard


class Mandelbrot(Game):
    # Attributes
    __cpos_x = 0  # cpos -> center pos
    __cpos_y = 0

    __scale = 1  # Effects visual scale and controls
    __iterations = 8  # Can be adjusted

    __SPEED = 10

    # Init
    def __init__(self):
        super().__init__()

    # Methods
    def next(self, dtime):
        if keyboard.is_pressed("a"):  # left
            self.set_cpos_x(self.get_cpos_x() - (dtime*self.__SPEED / self.get_scale()))

        if keyboard.is_pressed("d"):  # right
            self.set_cpos_x(self.get_cpos_x() + (dtime * self.__SPEED / self.get_scale()))

        if keyboard.is_pressed("w"):  # up
            self.set_cpos_y(self.get_cpos_y() - (dtime * self.__SPEED / self.get_scale()))

        if keyboard.is_pressed("s"):  # down
            self.set_cpos_y(self.get_cpos_y() + (dtime * self.__SPEED / self.get_scale()))

        if keyboard.is_pressed("j"):  # zoom in
            self.set_scale(self.get_scale() + dtime * self.get_scale())

        if keyboard.is_pressed("k"):  # zoom out
            self.set_scale(self.get_scale() - dtime * self.get_scale())

        if keyboard.is_pressed("l"):  # decrease iterations
            self.set_iterations(self.get_iterations() - 1)

        if keyboard.is_pressed(";"):  # increase iterations
            self.set_iterations(self.get_iterations() + 1)

    def render(self, x, y):
        brightness = [" ", ".", "*", "X", "#"]

        output = RenderLayer(x, y)

        for px in range(x):
            for py in range(int(y)):
                x0 = ((px - int(x/2)) / self.get_scale())/1.7 + self.get_cpos_x()
                y0 = (py - int(y/2)) / self.get_scale() + self.get_cpos_y()

                x1 = 0
                y1 = 0
                iters = 0

                while x1**2 + y1**2 <= 4 and iters < self.get_iterations() - 1:
                    xtemp = x1**2 - y1**2 + x0
                    y1 = 2*x1*y1 + y0
                    x1 = xtemp
                    iters += 1

                output.set_pixel(px, py, Pixel(brightness[int(iters/self.get_iterations() * len(brightness))]))

        return output

    # Getters
    def get_cpos_x(self):
        return self.__cpos_x

    def get_cpos_y(self):
        return self.__cpos_y

    def get_scale(self):
        return self.__scale

    def get_iterations(self):
        return self.__iterations

    # Setters
    def set_cpos_x(self, x):
        self.__cpos_x = x

    def set_cpos_y(self, y):
        self.__cpos_y = y

    def set_scale(self, scale):
        self.__scale = scale

    def set_iterations(self, iterations):
        self.__iterations = iterations

    # To string
    def __str__(self):
        pass

