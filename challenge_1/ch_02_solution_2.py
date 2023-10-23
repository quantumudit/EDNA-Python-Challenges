"""
Sum of 2 Numbers
=================================
Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
=================================

This module provides a function to calculate the sum of two numbers.
"""


def make_sum(num1: int, num2: int) -> int:
    """
    Calculate the sum of two numbers.

    Args:
        num1 (int): The first integer to be added.
        num2 (int): The second integer to be added.

    Returns:
        int: The sum of num1 and num2.

    Raises:
        ValueError: If either num1 or num2 is not an integer.
    """
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("num1 and num2 must be integers")
    return num1 + num2


if __name__ == "__main__":
    num1_a, num2_b = 1, 2
    num1_c, num2_d = 5, 2
    num1_e, num2_f = 4, 1

    print(f"The sum of {num1_a} and {num2_b} is {make_sum(num1_a, num2_b)}")
    print(f"The sum of {num1_c} and {num2_d} is {make_sum(num1_c, num2_d)}")
    print(f"The sum of {num1_e} and {num2_f} is {make_sum(num1_e, num2_f)}")
