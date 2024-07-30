#!/usr/bin/python3

def canUnlockAll(boxes):
    """Function that determines if all the boxes are opened.

    Number of boxes is n.
    Each box is numbered sequentially from 0 to n - 1 and each box may
    contain keys to the other boxes.
    Key with the same number as a box opens that box.
    You can assume all keys will be positive integers.
    There can be keys that do not have boxes.
    The first box boxes[0] is unlocked.

    Args:
        boxes: list of lists of integers.
    Returns:
        boolean: True if all boxes can be unlocked, otherwise False.
    """
    # Initialize set of visited boxes, starting with the first box
    visited = {0}
    # Initialize queue with the first box
    queue = [boxes[0]]
    # While there are boxes in the queue
    while queue:
        box = queue.pop(0)
        for key in box:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(boxes[key])
    return len(visited) == len(boxes)
