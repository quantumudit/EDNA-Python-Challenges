"""
The Caret Matcher
=============================
Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
=============================
This script demonstrates the use of regular expressions to find matches in a text.

The script defines a regular expression pattern to match non-word, non-whitespace characters
and searches for such matches in the given text. The matches are printed to the console.
"""

import re

TEXT = " alice15@gmail.com "
PATTERN = r"[^\w\s]"


matches = re.findall(PATTERN, TEXT)
print(f"Matches: {matches}")
