#!/usr/bin/python3
"""This module contains the second interview problem at A2SV"""
from collections import deque
from typing import List


def canUnlockAll(boxes: List[List[int]]):
    """determines if all boxes can be unlocked"""
    visited = set([0])
    queue = deque([0])
    openedBoxes = [0]

    while queue:
        node = queue.popleft()

        for neighbour in boxes[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                openedBoxes.append(neighbour)
    return True if len(openedBoxes) == len(boxes) else False
