#!/usr/bin/python3
"""Contains a method that determines if a given data set
represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Checks if a dataset is valid utf-8"""
    for value in data:
        if isinstance(value, int):
            if value < 0 or value > 255:
                return False
        elif isinstance(value, str):
            try:
                value.encode('utf-8').decode('utf-8')
            except UnicodeDecodeError:
                return False
    return True
