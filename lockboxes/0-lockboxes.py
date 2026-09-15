#!/usr/bin/python3
"""Module to check if all boxes can be opened"""


def canUnlockAll(boxes):
    """Try to open all boxes"""
    numBoxes = len(boxes)
    keys = list(boxes[0])
    unlocked = {0}

    while keys:
        currentKey = keys.pop() #return last key in keys
        if currentKey < numBoxes and currentKey not in unlocked:
            unlocked.add(currentKey)
            keys.extend(boxes[currentKey])

    return len(unlocked) == n
    