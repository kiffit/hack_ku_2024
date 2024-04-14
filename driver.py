# Thomas Safago
# 04/12/2024


import subprocess
import sys


from Window import Window
from GameBorder import GameBorder
from GameSelector import GameSelector


def main():
    try:
        if sys.argv[1:] == []:
            proc = subprocess.Popen(["echo", "Hello friend!"])
        else:
            proc = subprocess.Popen(sys.argv[1:])

        run = True

        while run:
            try:
                w1 = Window(proc)
                g1 = GameBorder(GameSelector())
                w1.run_game(g1)

                run = False

            except KeyboardInterrupt:
                print("\nExiting program")
                run = False

            except BaseException as e:
                print(f"Error occurred, resetting: {e}")

    except BaseException as e:
        print(f"MSG: Error has occurred: {e}")

    subprocess.Popen(["clear"])


if __name__ == '__main__':
    main()
