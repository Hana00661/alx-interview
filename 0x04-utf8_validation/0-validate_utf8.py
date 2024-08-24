#!/usr/bin/python3

""" 0-validate_utf8.py """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        A list of integers representing a data set.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """

    num_bytes = 0

    """ Check each byte in the data set"""

    for byte in data:
        """If this is the start of a new UTF-8 character"""

        if num_bytes == 0:
            """Check how many bytes this UTF-8 character contains"""

            if byte >> 5 == 0b110 or byte >> 5 == 0b1110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            """If this is not a continuation byte, return False"""
            if byte >> 6 != 0b10:
                return False
            """We've read a valid continuation byte"""
            num_bytes -= 1

    return num_bytes == 0
