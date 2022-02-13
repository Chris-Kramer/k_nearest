import geometry2D

def cilinder_volume(radius,height):
    """
    Returns the volume of a cilinder given its redius and height.

    >>> cilinder_volume(3,3)
    84.82300164692441
    """
    return geometry2D.circle_area(radius) * height

def square_prism_volume(side,height):
    """
    Returns the volume of a square prism given the side of its base and its height.

    >>> square prism_volume(3,3)
    27
    """
    return geometry2D.square_area(side) * height
