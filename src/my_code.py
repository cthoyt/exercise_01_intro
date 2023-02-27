"""This module ships code to implement some complex-valued math in python."""
from __future__ import annotations

from math import atan2, cos, sin, sqrt


def my_function() -> bool:
    """Return True immediately to demonstrate a working test.

    Returns:
        bool: Hardcoded to True.
    """
    return True


class Complex(object):
    """Implement a complex number class with addition and multiplication."""

    def __init__(self, realpart: float, imagpart: float):
        """Create a complex number object.

        Args:
            realpart (float): The real part of the number.
            imagpart (float): The complex part of the number.
        """
        # TODO: write me.

    def add(self, other: Complex) -> Complex:
        """Add to complex numbers.

        Compute (x_1 + jy_1) + (x_2 + jy_2) = x_1+x_2 + j(y_1 + y_2).

        Args:
            other (Complex): The number to add.

        Returns:
            Complex: A complex number object containig the sum of the two.
        """
        # TODO: implement me.
        return None

    def radius(self) -> float:
        """Compute the radius of the compelex number.

        According to Pythagoras, the radius is given by sqrt(x^2 + y^2)

        Returns:
            float: The radius of self.
        """
        # TODO: implement me.
        return None

    def angle(self) -> float:
        """Compute the angle of the complex number.

        For a complex number c = x + iy.
        The angle is typicall given by atan2(y, x)

        Returns:
            float: The angle of self.
        """
        # TODO: Implement me.
        return None

    def multiply(self, other: Complex) -> Complex:
        """Multiply two complex numbers (x_1 + jy_1) * (x_2 + jy_2).

        Complex numbers are often multiplied in polar form via
        c_mul = r_1*r_2e^(theta_1+theta_2).
        In other words the new radius is the product of the incoming radii.
        The new angle is given by the sum.
        Radius and angle can be converted back to the karthesian from via,
        x = r_mul cos( theta_mul),
        y = r_mul sin( theta_mul).

        Args:
            other (Complex): _description_

        Returns:
            Complex: The product of self and other.
        """
        # TODO: Implement me.
        return None

