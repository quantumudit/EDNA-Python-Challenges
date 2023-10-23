"""
Convert Minutes to Seconds
=================================
Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
=================================

This module provides a function to convert minutes to seconds.
"""


def convert(mins: int) -> int:
    """
    Convert minutes to seconds.

    Args:
        mins (int): The number of minutes to be converted to seconds.

    Returns:
        int: The equivalent number of seconds.

    Raises:
        ValueError: If the input 'mins' is not an integer.
    """
    if not isinstance(mins, int):
        raise ValueError('mins must be an integer')
    return mins * 60


if __name__ == "__main__":
    mins_a, mins_b, mins_c = 5, 3, 2
    print(f"{mins_a} minutes is {convert(mins_a)} seconds")
    print(f"{mins_b} minutes is {convert(mins_b)} seconds")
    print(f"{mins_c} minutes is {convert(mins_c)} seconds")
