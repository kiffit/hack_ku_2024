# Thomas Safago
# 04/13/2024


from Game import Game
from Pixel import Pixel
from RenderLayer import RenderLayer


import keyboard


class GameSelector(Game):
    # Attributes
    __cursor_x = 0
    __cursor_y = 0

    __window_x = 0
    __window_y = 0

    __cursor_image = RenderLayer(2, 1)

    __CURSOR_SPEED_X = 30
    __CURSOR_SPEED_Y = 15

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

        if keyboard.is_pressed("q"):
            return "GameSelector"

        self.__cursor_y = min(max(0, self.__cursor_y), self.__window_y-1)
        self.__cursor_x = min(max(0, self.__cursor_x), self.__window_x-2)

        if keyboard.is_pressed("space"):
            if self.__cursor_y < self.__window_y/2:
                if self.__cursor_x < self.__window_x/2:
                    return "Mandelbrot"
                else:
                    return "RenderTest"
            else:
                if self.__cursor_x < self.__window_x/2:
                    return "GameCanvas"
                else:
                    return "GameSnake"

    def render(self, x, y):
        output = RenderLayer(x, y)

        mandel = "* Mandelbrot Explorer *"
        rendertest = "* RenderTest *"
        gamecanvas = "* Drawing Canvas *"
        gamesnake = "* Sssnake *"

        mandel = make_layer_from_text(center_text_len(mandel, int(x/2)-3))
        rendertest = make_layer_from_text(center_text_len(rendertest, int(x / 2) - 2))
        gamecanvas = make_layer_from_text(center_text_len(gamecanvas, int(x / 2) - 2))
        gamesnake = make_layer_from_text(center_text_len(gamesnake, int(x / 2) - 2))

        for nx in range(x):
            for ny in range(y):
                if ny == int(y/2):
                    output.set_pixel(nx, ny, Pixel("-"))
                if nx == int(x/2):
                    output.set_pixel(nx, ny, Pixel("|"))
                if nx == int(x/2) and ny == int(y/2):
                    output.set_pixel(nx, ny, Pixel("+"))

        # Print headers
        output.add_layer(mandel, 1, int(y / 4))
        output.add_layer(rendertest, int(x / 2) + 1, int(y / 4))
        output.add_layer(gamecanvas, 1, int(3 * y / 4))
        output.add_layer(gamesnake, int(x / 2) + 1, int(3 * y / 4))

        i1 = make_layer_from_text("Use [W/A/S/D] to control the cursor.")
        i2 = make_layer_from_text("Use [SPACE] to confirm an option.")
        i3 = make_layer_from_text("Use [Q] in any page to return here, use [CTRL-C] to quit.")
        output.add_layer(i1, 0, 0)
        output.add_layer(i2, 0, 1)
        output.add_layer(i3, 0, 2)

        output.add_layer(self.__cursor_image, round(self.__cursor_x), round(self.__cursor_y))

        self.__window_x = x
        self.__window_y = y

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
