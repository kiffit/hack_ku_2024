# Thomas Safago
# 04/12/2024


import math

from Pixel import Pixel
from RenderLayer import RenderLayer


def main():
    r1 = RenderLayer(10, 10)
    r1.fill_layer(Pixel("u"))

    r2 = RenderLayer(2, 2)
    r2.fill_layer(Pixel("l"))

    print(r1.render_ascii())
    r1.add_layer(r2, 9, 9)
    print(r1.render_ascii())


if __name__ == '__main__':
    main()
