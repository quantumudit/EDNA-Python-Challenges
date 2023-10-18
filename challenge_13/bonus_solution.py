"""
Circle Class
=============================
Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
=============================

This script defines a Python class, Circle, for representing circles. The class provides methods for
manipulating and calculating properties of circles.
"""


class Circle:
    """Class representing a circle"""

    def __init__(self, radius: float):
        """
        Initialize a Circle object with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius
        self.pi = 3.14

    def get_radius(self) -> float:
        """
        Get the current radius of the circle.

        Returns:
            float: The radius of the circle.
        """
        return self.radius

    def set_radius(self, new_radius: float):
        """
        Set the radius of the circle to a new value.

        Args:
            new_radius (float): The new radius value to set.
        """
        self.radius = new_radius

    def calculate_area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.pi * (self.radius ** 2)

    def calculate_circumference(self) -> float:
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * self.pi * self.radius


if __name__ == '__main__':
    cir = Circle(radius=5)
    print(f"The radius of the circle is: {cir.get_radius()}")

    cir.set_radius(new_radius=10)
    print(f"The updated radius of the circle is: {cir.get_radius()}")

    calc_area = round(cir.calculate_area(), 2)
    print(f"The area of the circle is: {calc_area:.2f}")

    calc_peri = round(cir.calculate_circumference(), 2)
    print(f"The circumference of the circle is: {calc_peri:.2f}")
