#!/usr/bin/python3
"""
0-making_change.py"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount
    """
    counter = 0
    if total <= 0:
        return 0
    if not coins:
        return -1
    if min(coins) > total:
        return -1
    if sum(coins) == total:
        return len(coins)
    if total in coins:
        return 1
    sort = sorted(coins, reverse=True)

    for i in range(len(sort)):
        while sort[i] <= total:
            total = total - sort[i]
            counter += 1

    if total == 0:
        return counter
        # box.append(counter)
    return -1
