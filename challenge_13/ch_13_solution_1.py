"""
Count Characters in a String
=================================
Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
=================================

This script defines a function, count_chars, which counts the frequency of each character
in a given input string and returns a dictionary with characters as keys and their 
respective counts as values.
"""


def count_chars(text: str) -> dict:
    """
    Count the frequency of each character in the input text and return a dictionary
    with characters as keys and their respective counts as values.

    Args:
    text (str): The input text to analyze.

    Returns:
    dict: A dictionary where keys are characters and values are their counts.
    """
    # Convert the input text to a list of characters
    char_list = [char for char in text]

    char_count = {}

    for char in char_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


if __name__ == "__main__":
    WORD = "banana"
    result = count_chars(text=WORD)
    print(result)
