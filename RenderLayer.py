# Thomas Safago
# 04/12/2024


"""
A render layer is an x-y grid of pixels. Thus, a convention must be set.
The standard convention for drawing screens is as follows for m,n pixels.

0,0 0,1 0,2 ... 0,n-1
1,0 1,1 1,2 ... 1,n-1
2,0 2,1 2,2 ... 2,n-1
...
m-1,0 m-1,1 m-1,2 ... m-1,n-1

Render layers will arrange their nested lists as such:

[ ] [ ] [ ]
 |   |   |
[ ] [ ] [ ]
 |   |   |
[ ] [ ] [ ]

this allows for intuitive access of [x][y]
"""


from Pixel import Pixel


class RenderLayer:
    # Attributes
    __data = None  # Will be a 2-dimensional list ordered as above

    __x = -1
    __y = -1

    # Init
    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)

        # Init multidimensional array with blank pixels
        self.set_data([[Pixel() for _ in range(self.get_y())] for _ in range(self.get_x())])

    # Helpers
    def set_pixel(self, x, y, pixel=Pixel()):
        self.get_data()[x][y] = pixel

    def get_pixel(self, x, y):
        return self.get_data()[x][y]

    def fill_layer(self, pixel=Pixel()):
        for y in range(self.get_y()):
            for x in range(self.get_x()):
                self.set_pixel(x, y, pixel)

    def clear_layer(self):
        self.fill_layer()

    def add_layer(self, layer, x=0, y=0):
        # Will add another layer onto this one, where the corner of that layer is overlaid based on x, y
        cx = min(x, self.get_x())  # Corner x and y points
        cy = min(y, self.get_y())

        ex = min(self.get_x(), x + layer.get_x())  # Other corner x and y
        ey = min(self.get_y(), y + layer.get_y())

        for lx in range(cx, ex):
            for ly in range(cy, ey):
                self.set_pixel(lx, ly, layer.get_pixel(lx - cx, ly - cy))

    def render_ascii(self):
        output = ""

        for y in range(self.get_y()):
            for x in range(self.get_x()):
                output += self.get_pixel(x, y).draw()
            output += "\n"

        return output

    # Getters
    def get_data(self):
        return self.__data

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    # Setters
    def set_data(self, data):
        self.__data = data

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    # To string
    def __str__(self):
        pass
