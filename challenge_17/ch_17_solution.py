"""
Even-Odd & Sign Check
================================================
Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
================================================

This script provides a function to check whether a given integer is positive, negative, 
or zero, and if it's even or odd. The function returns a tuple with two strings: 
the first indicates the number's sign (positive, negative, or zero), and 
the second specifies its parity (even or odd).
"""


def check_num(num: int) -> tuple:
    """
    Determine whether a given number is positive, negative, or zero and whether it is even or odd.

    Args:
        num (int): The integer number to be checked.

    Returns:
        tuple: A tuple containing two strings:
            - The first string indicates whether the number is "positive," "negative," or "zero."
            - The second string indicates whether the number is "even" or "odd."
    """
    num_sign = "positive" if num > 0 else "negative"
    even_odd = "even" if num % 2 == 0 else "odd"

    return (num_sign, even_odd)


if __name__ == "__main__":
    NUM_INPUT = input("Provide a number: ")
    try:
        number = int(NUM_INPUT)
        if number == 0:
            print("The number is zero")
        else:
            result = check_num(num=number)
            print(f"The number {number} is a {result[0]} {result[1]} number")
    except ValueError:
        print("Input number is not an integer")
