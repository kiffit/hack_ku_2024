# Thomas Safago
# 04/13/2024


from Game import Game
from Pixel import Pixel
from RenderLayer import RenderLayer


from Mandelbrot import Mandelbrot
from RenderTest import RenderTest
from GameCanvas import GameCanvas
from GameSnake import GameSnake


from GameSelector import GameSelector


class GameBorder(Game):
    # Attributes
    __sub_game = None  # Underlying game

    __SIDE_CHAR = "|"
    __UPPER_CHAR = "-"
    __CORNER_CHAR = "+"

    # Init
    def __init__(self, game=RenderTest()):
        super().__init__()
        self.set_sub_game(game)

    # Methods
    def next(self, dtime):
        game = self.get_sub_game().next(dtime)
        if game is not None:
            if game == "GameSelector":
                self.set_sub_game(GameSelector())
            elif game == "Mandelbrot":
                self.set_sub_game(Mandelbrot())
            elif game == "RenderTest":
                self.set_sub_game(RenderTest())
            elif game == "GameCanvas":
                self.set_sub_game(GameCanvas())
            elif game == "GameSnake":
                self.set_sub_game(GameSnake())

    def render(self, x, y, pid_status):
        """
        The top three lines are reserved for the titlebar which will eventually specify progress
        A border will surround the window otherwise
        """

        overlay = RenderLayer(x, y)
        msg = None

        running = center_text_len("Process is running...", x-2)
        finished = center_text_len("Process is finished!", x - 2)

        if pid_status:
            msg = make_layer_from_text(running, bcolors.BOLD + bcolors.UNDERLINE + bcolors.REDBG)
        else:
            msg = make_layer_from_text(finished, bcolors.BOLD + bcolors.UNDERLINE + bcolors.GREENBG)

        for nx in range(x):
            for ny in range(y):
                if nx == 0 or nx == x-1:
                    overlay.set_pixel(nx, ny, Pixel(self.__SIDE_CHAR))
                elif ny == 0 or ny == 2 or ny == y-1:
                    overlay.set_pixel(nx, ny, Pixel(self.__UPPER_CHAR))

                if (ny == 0 or ny == 2 or ny == y-1) and (nx == 0 or nx == x-1):
                    overlay.set_pixel(nx, ny, Pixel(self.__CORNER_CHAR))

        game = self.get_sub_game().render(x-2, y-4)
        overlay.add_layer(game, 1, 3)
        overlay.add_layer(msg, 1, 1)

        return overlay

    # Getters
    def get_sub_game(self):
        return self.__sub_game

    # Setters
    def set_sub_game(self, sub_game):
        self.__sub_game = sub_game

    # To string
    def __str__(self):
        pass


# Utility functions
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
