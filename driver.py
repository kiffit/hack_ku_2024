# Thomas Safago
# 04/12/2024


import math

from Pixel import Pixel
from RenderLayer import RenderLayer
from RenderQueue import RenderQueue


import subprocess
import shlex
import sys


from Window import Window
from GameBorder import GameBorder
from Mandelbrot import Mandelbrot


def main():
    try:
        proc = subprocess.Popen(sys.argv[1:])

        run = True

        while run:
            try:
                w1 = Window(proc)
                g1 = GameBorder(Mandelbrot())
                w1.run_game(g1)

                run = False

            except KeyboardInterrupt as e:
                print("\nExiting program")
                run = False

            except BaseException as e:
                print(f"Error occurred, resetting: {e}")

    except BaseException as e:
        print(f"MSG: Error has occurred: {e}")


if __name__ == '__main__':
    main()
