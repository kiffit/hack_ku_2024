# Thomas Safago
# 04/13/2024


from Game import Game
from Pixel import Pixel
from RenderLayer import RenderLayer


import keyboard


class Mandelbrot(Game):
    # Attributes
    __cpos_x = 0  # cpos -> center pos
    __cpos_y = 0

    __scale = 1  # Effects visual scale and controls
    __iterations = 8  # Can be adjusted

    __SPEED = 10

    __SPEED_MULT = 3

    # Init
    def __init__(self):
        super().__init__()

    # Methods
    def next(self, dtime):
        spd = self.__SPEED

        if keyboard.is_pressed("shift"):
            spd *= self.__SPEED_MULT

        if keyboard.is_pressed("a"):  # left
            self.set_cpos_x(self.get_cpos_x() - (dtime * spd / self.get_scale()))

        if keyboard.is_pressed("d"):  # right
            self.set_cpos_x(self.get_cpos_x() + (dtime * spd / self.get_scale()))

        if keyboard.is_pressed("w"):  # up
            self.set_cpos_y(self.get_cpos_y() - (dtime * spd / self.get_scale()))

        if keyboard.is_pressed("s"):  # down
            self.set_cpos_y(self.get_cpos_y() + (dtime * spd / self.get_scale()))

        if keyboard.is_pressed("j"):  # zoom in
            self.set_scale(self.get_scale() + dtime * self.get_scale())

        if keyboard.is_pressed("k"):  # zoom out
            self.set_scale(self.get_scale() - dtime * self.get_scale())

        if keyboard.is_pressed("l"):  # decrease iterations
            self.set_iterations(self.get_iterations() - 1)

        if keyboard.is_pressed(";"):  # increase iterations
            self.set_iterations(self.get_iterations() + 1)

        if keyboard.is_pressed("q"):
            return "GameSelector"

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

        i1 = make_layer_from_text("[W/A/S/D] to navigate, [j/k] to zoom, [l/;] to increase samples.")
        i2 = make_layer_from_text(f"Scale: {round(self.get_scale(), 4)}, Iterations: {self.get_iterations()}")

        output.add_layer(i1, 0, 0)
        output.add_layer(i2, 0, 1)

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


# Utility
class bcolors:
    REDBG = '\033[41m'
    GREENBG = '\033[42m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def make_layer_from_text(text, color=bcolors.BOLD):
    layer = RenderLayer(len(text), 1)

    for i, char in enumerate(text):
        layer.set_pixel(i, 0, Pixel(color + char + bcolors.ENDC))

    return layer


def center_text_len(text, length):
    nlength = int((length - len(text))/2)
    text = (" " * nlength) + text + (" " * nlength)

    if len(text) != length:
        text += " "

    return text
