#!/usr/bin/python3
"""this module contains function for lockboxes"""


def canUnlockAll(boxes):
    """weheter the boxes can be opended or not"""
    keys = []
    opend_boxes = []
    for i in range(len(boxes[0])):
        keys.append(boxes[0][i])
    opend_boxes.append(0)
    while keys:
        temp_key = keys.pop()
        if temp_key < len(boxes) and temp_key not in opend_boxes:
            opend_boxes.append(temp_key)
            for i in range(len(boxes[temp_key])):
                keys.append(boxes[temp_key][i])
                keys = list(set(keys))
    return len(boxes) == len(opend_boxes)
