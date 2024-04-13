# Thomas Safago
# 04/13/2024


from Game import Game
from Pixel import Pixel
from RenderLayer import RenderLayer
from RenderTest import RenderTest


import keyboard


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
        self.get_sub_game().next(dtime)

    def render(self, x, y):
        """
        The top three lines are reserved for the titlebar which will eventually specify progress
        A border will surround the window otherwise
        """

        overlay = RenderLayer(x, y)

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

