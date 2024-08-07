#!/usr/bin/python3
"""
0-minoperations.py"""


def minOperations(n):
    """calculates the fewest number of operations
        needed to result in exactly n H characters in the file.
    Returns:
        int: The number of minimal operations needed to get n H characters
    or 0 if it is impossible to achieve n.
    """
    pasted_chars = 1
    clipboard = 0
    counter = 0

    while pasted_chars < n:
        if clipboard == 0:
            clipboard = pasted_chars
            counter += 1

        if pasted_chars == 1:
            pasted_chars += clipboard
            counter += 1
            continue

        remaining = n - pasted_chars # remaining chars to Paste
        if remaining < clipboard:
            return 0
        # check if can paste
        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            counter += 1
        else:
            clipboard = pasted_chars
            pasted_chars += clipboard
            counter += 2
    if pasted_chars == n:
        return counter
    else:
        return 0