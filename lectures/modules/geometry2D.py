from math import pi

def circle_area(radius):
    """
    Returns the area of a circle given its radius.

    >>> circle_area(3)
    28.274333882308138
    """
    return pi * radius ** 2


def square_area(side):
    """
    Returns the area of a square given the length of its side.

    >>> square_area(3)
    9
    """
    return side ** 2
