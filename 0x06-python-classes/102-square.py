#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """
    Class Square that defines a square.

    Attributes:
        __size (float or int): Private instance attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (float or int, optional): The size of the square. Default is 0.
        """
        self.size = size  # Using the setter to perform validation

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
            value (float or int): The value to set as the size of the square.

        Raises:
            TypeError: If value is not a number (float or int).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Override the equality operator (==) based on the square area.

        Parameters:
            other (Square): The other square to compare.

        Returns:
            bool: True if the square areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Override the not equal operator (!=) based on the square area.

        Parameters:
            other (Square): The other square to compare.

        Returns:
            bool: True if the square areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Override the less than operator (<) based on the square area.

        Parameters:
            other (Square): The other square to compare.

        Returns:
            bool: True if the square area is less than the other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Override the less than or equal operator (<=) based on the square area.

        Parameters:
            other (Square): The other square to compare.

        Returns:
            bool: True if the square area is less than or equal to the other, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Override the greater than operator (>) based on the square area.

        Parameters:
            other (Square): The other square to compare.

        Returns:
            bool: True if the square area is greater than the other, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Override the greater than or equal operator (>=) based on the square area.

        Parameters:
            other (Square): The other square to compare.

        Returns:
            bool: True if the square area is greater than or equal to the other, False otherwise.
        """
        return self.area() >= other.area()
