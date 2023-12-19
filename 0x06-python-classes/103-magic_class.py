#!/usr/bin/python3
"""Defines a class MagicShape"""
import math


class MagicShape:
    """
    Class that defines properties of MagicShape.

    Attributes:
        radius: Radius of the shape.
    """
    def __init__(self, radius=0):
        """Creates new instances of MagicShape.

        Args:
            radius: Radius of the shape.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def calculate_area(self):
        """Returns the area of the shape.

        Returns:
            float: Area of the shape.
        """
        return math.pi * self.__radius ** 2

    def calculate_circumference(self):
        """Returns the circumference of the shape.

        Returns:
            float: Circumference of the shape.
        """
        return 2 * math.pi * self.__radius
