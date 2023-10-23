"""
Calculator Class
=============================
Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
=============================
This module defines the Calculator class for basic arithmetic operations.
The operation involves: addition, subtraction, multiplication and division

"""


class Calculator:
    """Class representing a calculator"""

    def __init__(self, num1: int, num2: int):
        """
        Initialize a Calculator object with two numbers.

        Args:
            num1 (int): The first integer for calculations.
            num2 (int): The second integer for calculations.
        Raises:
            ValueError: If num1 or num2 is not an integer
        """
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise ValueError("Both num1 and num2 must be integers.")

        self.num1 = num1
        self.num2 = num2

    def add(self) -> int:
        """
        Add two numbers and return the result.

        Returns:
            int: The sum of num1 and num2.
        """
        return self.num1 + self.num2

    def subtract(self) -> int:
        """
        Subtract the second number from the first and return the result.

        Returns:
            int: The result of num1 - num2.
        """
        return self.num1 - self.num2

    def multiply(self) -> int:
        """
        Multiply two numbers and return the result.

        Returns:
            int: The product of num1 and num2.
        """
        return self.num1 * self.num2

    def divide(self) -> float:
        """
        Divide the first number by the second and return the result as a float.

        Returns:
            float: The result of num1 / num2.

        Raises:
            ValueError: If num2 is zero.
        """
        if self.num2 == 0:
            return ValueError("Division by zero is not allowed.")
        return self.num1 / self.num2


if __name__ == '__main__':
    calculator = Calculator(num1=0, num2=0)

    print(f"Given 2 numbers: {calculator.num1} and {calculator.num2}")
    print("The results of basic arithmetic operations over the 2 numbers are:")
    print(f"Addition: {calculator.add()}")
    print(f"Subtraction: {calculator.subtract()}")
    print(f"Multiplication: {calculator.multiply()}")
    print(f"Division: {calculator.divide()}")
