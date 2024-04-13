# Thomas Safago
# 04/12/2024

"""
Render queue: a list of items queued to render
This will store render layers
Rendering the render queue:
    use clear command for linux terminal
    beginning at index 0, add following layers IF draw for that layer is on into a new layer
    print that layer
"""


from RenderLayer import RenderLayer


class RenderQueue:
    # Attributes
    __queue = []

    # Init
    def __init__(self, *args):
        for layer in args:
            self.append(layer)

    # Methods
    def append(self, *layers):
        for layer in layers:
            self.get_queue().append(layer)

    def insert(self, layer, loc=0):
        self.get_queue().insert(layer, loc)

    def pop(self, loc):
        self.get_queue().pop(loc)

    def clear_queue(self):
        self.set_queue([])

    # Helpers
    def render_as_layer(self):
        i = 0

        while not self.get_queue()[i].get_draw() and i < len(self.get_queue())-1:
            i += 1

        layer = self.get_queue()[i]

        for j in range(i, len(self.get_queue())):
            if self.get_queue()[j].get_draw():
                layer.add_layer(self.get_queue()[j],
                                self.get_queue()[j].get_offset_x(),
                                self.get_queue()[j].get_offset_y())

        return layer

    def render_ascii(self):
        return self.render_as_layer().render_ascii()

    # Getters
    def get_queue(self):
        return self.__queue

    def get_draw(self):
        return self.__draw

    # Setters
    def set_queue(self, queue):
        self.__queue = queue

    def set_draw(self, draw):
        self.__draw = draw

    # To string
    def __str__(self):
        ret_str = "RenderQueue:"

        for index, layer in enumerate(self.get_queue()):
            ret_str += f"\n{index} -> {layer}"

        return ret_str
