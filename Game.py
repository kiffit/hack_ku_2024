# Thomas Safago
# 04/13/2024


from abc import ABC, abstractmethod


class Game(ABC):
    # Attributes

    # Init
    @abstractmethod
    def __init__(self):
        ...

    # Methods
    @abstractmethod
    def next(self, dtime):  # Steps game. All game logic should occur here
        ...

    @abstractmethod
    def render(self, x, y):  # Must return frame as a RenderLayer in size x,y
        ...

    # Getters

    # Setters

    # To string
    def __str__(self):
        pass
