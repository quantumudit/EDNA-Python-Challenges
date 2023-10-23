"""
FizzBuzz
=================================
Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
=================================

This module provides a function to play the FizzBuzz game.
"""


def fizzbuzz(num: int) -> str:
    """
    Play the FizzBuzz game with the given number.

    Args:
        num (int): The number to be evaluated for FizzBuzz.

    Returns:
        str: "Fizz" if num is divisible by 3, "Buzz" if divisible by 5,
        "FizzBuzz" if divisible by both 3 and 5, or the input number
        as a string if none of the conditions are met.

    Raises:
        ValueError: If the input 'num' is not an integer.
    """
    if not isinstance(num, int):
        raise ValueError("Input number must be an integer")

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


if __name__ == "__main__":
    NUM = 15
    print(fizzbuzz(NUM))
