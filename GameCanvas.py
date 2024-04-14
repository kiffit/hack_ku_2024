# Thomas Safago
# 04/13/2024


from Game import Game
from Pixel import Pixel
from RenderLayer import RenderLayer


import keyboard


class GameCanvas(Game):
    # Attributes
    __cursor_x = 0
    __cursor_y = 0

    __window_x = 0
    __window_y = 0

    __cursor_image = RenderLayer(2, 1)

    __CURSOR_SPEED_X = 30
    __CURSOR_SPEED_Y = 15

    __drawn_pixels = set()

    # Init
    def __init__(self):
        super().__init__()
        self.__cursor_image.set_pixel(0, 0, Pixel("["))
        self.__cursor_image.set_pixel(1, 0, Pixel("]"))

    # Methods
    def next(self, dtime):
        if keyboard.is_pressed("w"):
            self.__cursor_y -= (dtime * self.__CURSOR_SPEED_Y)
        if keyboard.is_pressed("s"):
            self.__cursor_y += (dtime * self.__CURSOR_SPEED_Y)
        if keyboard.is_pressed("a"):
            self.__cursor_x -= (dtime * self.__CURSOR_SPEED_X)
        if keyboard.is_pressed("d"):
            self.__cursor_x += (dtime * self.__CURSOR_SPEED_X)
        if keyboard.is_pressed("c"):
            self.__drawn_pixels = set()

        if keyboard.is_pressed("q"):
            return "GameSelector"

        self.__cursor_y = min(max(0, self.__cursor_y), self.__window_y-1)
        self.__cursor_x = min(max(0, self.__cursor_x), self.__window_x-2)

        if keyboard.is_pressed("space"):
            self.__drawn_pixels.add((round(self.__cursor_x), round(self.__cursor_y)))

    def render(self, x, y):
        output = RenderLayer(x, y)

        for pixels in self.__drawn_pixels:
            output.set_pixel(pixels[0], pixels[1], Pixel("#"))

        output.add_layer(self.__cursor_image, round(self.__cursor_x), round(self.__cursor_y))

        self.__window_x = x
        self.__window_y = y

        i1 = make_layer_from_text("Use [W/A/S/D] to navigate, hold [SPACE] to draw. Press [C] to clear buffer.")
        output.add_layer(i1)

        return output

    # Getters

    # Setters

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
