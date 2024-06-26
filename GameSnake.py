# Thomas Safago
# 04/13/2024


from Game import Game
from Pixel import Pixel
from RenderLayer import RenderLayer


import random
import keyboard


class GameSnake(Game):
    # Attributes
    __snake_body = []
    __dir = "None"
    __apples = []
    __frame = 0
    __has_eaten = False

    __window_x = 10
    __window_y = 10

    __ox = 0
    __oy = 0

    __SPEED = 10
    __SPEED_BOOST = 2

    # Init
    def __init__(self):
        super().__init__()
        self.init_snake_board()

    # Methods
    def next(self, dtime):
        cpos = self.__snake_body[0]
        if not (0 <= cpos[0] < self.__window_x-1) or not (0 <= cpos[1] < self.__window_y-1):
            return "GameSelector"

        for snek in self.__snake_body[1:]:
            if self.__snake_body[0][0] == snek[0] and self.__snake_body[0][1] == snek[1]:
                return "GameSelector"

        self.__frame += 1
        spd = self.__SPEED

        if keyboard.is_pressed("shift"):
            spd /= self.__SPEED_BOOST

        if self.__frame % spd == 0:
            self.__has_eaten = False
            if self.__ox != self.__window_x or self.__oy != self.__window_y:
                self.init_snake_board()
                self.__oy = self.__window_y
                self.__ox = self.__window_x

            if keyboard.is_pressed("s"):
                if self.__dir != "down":
                    self.__dir = "up"

            elif keyboard.is_pressed("w"):
                if self.__dir != "up":
                    self.__dir = "down"

            elif keyboard.is_pressed("a"):
                if self.__dir != "right":
                    self.__dir = "left"

            elif keyboard.is_pressed("d"):
                if self.__dir != "left":
                    self.__dir = "right"

            for apple in self.__apples:
                pos = self.__snake_body[0]
                if pos[0] == apple[0] and pos[1] == apple[1]:
                    self.__has_eaten = True
                    self.__apples.remove(apple)
                    self.gen_apple()

            if not self.__has_eaten:
                self.__snake_body.remove(self.__snake_body[-1])  # hehe

            if self.__dir == "up":
                self.__snake_body.insert(0, [self.__snake_body[0][0], self.__snake_body[0][1] + 1])
            elif self.__dir == "down":
                self.__snake_body.insert(0, [self.__snake_body[0][0], self.__snake_body[0][1] - 1])
            elif self.__dir == "left":
                self.__snake_body.insert(0, [self.__snake_body[0][0] - 1, self.__snake_body[0][1]])
            elif self.__dir == "right":
                self.__snake_body.insert(0, [self.__snake_body[0][0] + 1, self.__snake_body[0][1]])

        if keyboard.is_pressed("q"):
            return "GameSelector"

    def gen_apple(self):
        apple = [random.randint(0, self.__window_x-1), random.randint(0, self.__window_y-1)]
        for snek in self.__snake_body:
            if apple[0] == snek[0] and apple[1] == snek[1]:
                apple = [random.randint(0, self.__window_x), random.randint(0, self.__window_y)]

        self.__apples.append(apple)

    def render(self, x, y):
        self.__window_x = x
        self.__window_y = y

        output = RenderLayer(x, y)

        for segment in self.__snake_body:
            output.set_pixel(segment[0], segment[1], Pixel("#"))

        for apple in self.__apples:
            output.set_pixel(apple[0], apple[1], Pixel("@"))

        pos = self.__snake_body[0]
        output.set_pixel(pos[0], pos[1], Pixel("O"))

        instructions = make_layer_from_text("Use WASD to move")
        output.add_layer(instructions, 0, 0)

        return output

    def init_snake_board(self):
        middle = [round(self.__window_x/2), round(self.__window_y/2)]
        self.__snake_body = []
        self.__snake_body.append(middle)
        self.__snake_body.append([middle[0], middle[1] + 1])
        self.__snake_body.append([middle[0], middle[1] + 2])
        self.__snake_body.append([middle[0], middle[1] + 3])
        self.__dir = "down"
        self.__frame = 0
        self.__has_eaten = False

        self.__apples = []
        for _ in range(10):
            self.gen_apple()

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
