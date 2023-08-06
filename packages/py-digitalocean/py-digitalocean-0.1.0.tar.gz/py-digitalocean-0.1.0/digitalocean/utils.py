"""
Common Utility Functions
"""
import re

def validate_list_of_strings(strings):
    """Validates a list is a list of strings

        Args:
            strings (:type: list of str): List of strings

        Raises:
            ValueError - One element of list is not a string
    """
    for string in strings:
        if not isinstance(string, str):
            raise ValueError

def validate_list_of_ints(ints):
    """Validates a list is a list of ints

        Args:
            ints (:type: list of int): List of ints

        Raises:
            ValueError - One element of list is not an integer
    """
    for i in ints:
        if not isinstance(i, int):
            raise ValueError

def validate_date_time(date_time):
    """Validate Date and Time is ISO8601 Format

        Args:
            date_time (str): Date and Time string

        Raises:
            ValueError: String was not of ISO8601 Format
    """
    regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])' \
            '-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):'\
            '([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?'\
            '(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'

    date_time_match = re.compile(regex).match
    if date_time_match(date_time) is None:
        raise ValueError
