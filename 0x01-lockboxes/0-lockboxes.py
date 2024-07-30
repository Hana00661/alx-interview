#!/usr/bin/python3
""" implements a breadth-first search (BFS) algorithm
 to solve this problem.
"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes are opened.

    Number of boxes is n.
    Each box is numbered sequentially from 0 to n - 1 and each box may
    Args:
        boxes: list of lists of integers.

    Returns:
        True if all boxes can be unlocked, otherwise False.
    """
    # set of visited boxes, starting with the first box
    visited = {0}
    # queue with the first box
    queue = [boxes[0]]
    # While there are boxes in the queue
    while queue:
        # Take the first box from the queue
        box = queue.pop(0)
        # Iterate through the keys in the box
        for key in box:
            # If the key corresponds to a locked box
            if key not in visited and key < len(boxes):
                # Mark the box as visited
                visited.add(key)
                # Add the box to the queue to explore its keys
                queue.append(boxes[key])
    # Return whether all boxes have been visited
    return len(visited) == len(boxes)
