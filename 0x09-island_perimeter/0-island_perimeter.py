#!/usr/bin/python3
"""Defines the island_perimeter function that finds the perimeter of
and island in a grid"""
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """Returns the perimeter of an island in a given grid"""
    result = 0
    visited = set()
    r, c = len(grid), len(grid[0])

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    def inbound(row: int, col: int) -> bool:
        """checks if a node is in the grid"""
        return 0 <= row < r and 0 <= col < c and grid[row][col] != 0

    def find_perimeter(row: int, col: int) -> int:
        """returns the perimeter of the island"""
        if not inbound(row, col):
            return 1

        local = 0
        visited.add((row, col))
        for rInc, cInc in directions:
            newR, newC = row + rInc, col + cInc
            if (newR, newC) not in visited:
                local += find_perimeter(newR, newC)
        return local

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1 and (i, j) not in visited:
                result = find_perimeter(i, j)

    return result
