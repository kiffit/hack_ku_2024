# Thomas Safago
# 04/12/2024


import math

from Pixel import Pixel
from RenderLayer import RenderLayer
from RenderQueue import RenderQueue
from Window import Window
from GameBorder import GameBorder


def main():
    w1 = Window()
    g1 = GameBorder()

    w1.run_game(g1)


if __name__ == '__main__':
    main()
