# Thomas Safago
# 04/12/2024


"""
This class will handle keyboard input, program open/closing, PID monitoring, outputting to screen and fps control.
First challenge: let program run at user-definable fps
"""


import os
import time

import keyboard
from RenderLayer import RenderLayer
from RenderQueue import RenderQueue
from Pixel import Pixel


class Window:
    # Attributes
    __x = -1
    __y = -1
    __game_x = -1
    __game_y = -1

    __queue = RenderQueue()  # Will be a render queue

    __game_running = False
    __FPS = 60

    # Init
    def __init__(self):
        self.set_dimensions()

    # Methods
    def set_dimensions(self):
        terminal = os.get_terminal_size()

        self.set_x(terminal[0]-1)
        self.set_y(terminal[1]-1)

        self.set_game_x(terminal[0])
        self.set_game_y(terminal[1]-1)

    def run_game(self, game):
        start = 0  # Frame time controls
        end = 0
        dtime = 1

        self.set_game_running(True)

        while self.is_game_running():
            end = time.time()  # End time
            dtime = end - start
            start = time.time()  # Start timer

            # Begin rendering window
            self.get_queue().clear_queue()

            # Adjust window dimensions
            self.set_dimensions()

            # Render game
            game.next(dtime)
            self.get_queue().append(game.render(self.get_game_x(), self.get_game_y()))

            # Output rendered
            # os.system("clear")
            print(self.get_queue().render_ascii(), end="")

            # Pause if necessary for frame limiter
            if dtime < 1/self.__FPS:
                time.sleep(1/self.__FPS - dtime)

        self.set_game_running(False)

    # Getters
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_game_x(self):
        return self.__game_x

    def get_game_y(self):
        return self.__game_y

    def get_queue(self):
        return self.__queue

    def is_game_running(self):
        return self.__game_running

    # Setters
    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_game_x(self, x):
        self.__game_x = x

    def set_game_y(self, y):
        self.__game_y = y

    def set_game_running(self, status):
        self.__game_running = status

    # To string
    def __str__(self):
        pass
