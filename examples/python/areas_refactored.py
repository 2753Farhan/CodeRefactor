"""Concise area computation helpers.

This module contains simple helper functions to calculate areas. It
is intentionally small and focused so it can be used by the test suite
and by demonstration scripts.
"""
from __future__ import annotations

import math
from typing import Union


def calculate_area_of_rectangle(length: Union[int, float], width: Union[int, float]) -> float:
    """Return the area of a rectangle using length * width.

    Args:
        length: rectangle length
        width: rectangle width

    Returns:
        The numeric area as a float.
    """
    return float(length * width)


def calculate_area_of_circle(radius: Union[int, float]) -> float:
    """Return the area of a circle based on the provided radius.

    Args:
        radius: the radius of the circle

    Returns:
        The area as a float (pi * r^2).
    """
    return math.pi * (radius ** 2)


if __name__ == "__main__":
    # Example usage for demonstration; the value printouts stay the
    # same as the original implementation to show no functional change.
    print(f"Area of rectangle: {calculate_area_of_rectangle(10, 5)}")
    print(f"Area of circle: {calculate_area_of_circle(7)}")

"""Concise area computation helpers.

This module contains simple helper functions to calculate areas. It
is intentionally small and focused so it can be used by the test suite
and by demonstration scripts.
"""
from __future__ import annotations

import math
from typing import Union


def calculate_area_of_rectangle(length: Union[int, float], width: Union[int, float]) -> float:
    """Return the area of a rectangle using length * width.

    Args:
        length: rectangle length
        width: rectangle width

    Returns:
        The numeric area as a float.
    """
    return float(length * width)


def calculate_area_of_circle(radius: Union[int, float]) -> float:
    """Return the area of a circle based on the provided radius.

    Args:
        radius: the radius of the circle

    Returns:
        The area as a float (pi * r^2).
    """
    return math.pi * (radius ** 2)


if __name__ == "__main__":
    # Example usage for demonstration; the value printouts stay the
    # same as the original implementation to show no functional change.
    print(f"Area of rectangle: {calculate_area_of_rectangle(10, 5)}")
    print(f"Area of circle: {calculate_area_of_circle(7)}")
