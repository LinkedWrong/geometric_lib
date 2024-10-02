import math


def area(r):
    """Calculates the area of a circle.

    Args:
        r: The radius of the circle.

    Returns:
        The area of the circle.
    """
    return math.pi * r * r


def perimeter(r):
    """Calculates the perimeter of a circle (also known as the circumference).

    Args:
        r: The radius of the circle.

    Returns:
        The perimeter of the circle.
    """
    return 2 * math.pi * r
