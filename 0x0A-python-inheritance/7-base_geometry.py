#!/usr/bin/python3
"""Module for BaseGeometry class with integer validation"""

class BaseGeometry:
    """A base geometry class with integer validation"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
