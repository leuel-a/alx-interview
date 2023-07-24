#!/usr/bin/python3
"""ALX Interview Prep --> Pascal's Triangle"""
from typing import List, Optional, Sequence


def pascal_triangle(n: int) -> List[List[int]]:
    """Returns a list of lists of integers representing the Pascal's triangle"""

    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(n):
        curr = pascal[-1]
        row = [1]

        for j in range(len(curr) - 1):
            row.append(curr[j] + curr[j + 1])
        row.append(1)

        pascal.append(row)
    return pascal[:-1]

