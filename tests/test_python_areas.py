import math
from examples.python.areas_refactored import calculate_area_of_rectangle, calculate_area_of_circle


def test_rectangle_area():
    assert calculate_area_of_rectangle(10, 5) == 50


def test_circle_area():
    assert math.isclose(calculate_area_of_circle(7), math.pi * 49)
