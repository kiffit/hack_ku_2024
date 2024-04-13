# Thomas Safago
# 04/12/2024


"""
A pixel is the most basic abstraction and for this case, should represent a simple character.
Using a class will allow for extensibility into colors later.
"""


class Pixel:
    # Attributes
    __value = ""

    # Init
    def __init__(self, value=" "):
        self.set_value(value)

    # Methods
    def draw(self):
        return self.get_value()

    # Getters
    def get_value(self):
        return self.__value

    # Setters
    def set_value(self, value):
        self.__value = value

    # To string
    def __str__(self):
        return (
            f"Pixel:"
            f"\n\tValue: {self.get_value()}"
        )
