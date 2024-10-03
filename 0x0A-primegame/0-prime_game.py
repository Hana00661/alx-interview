#!/usr/bin/python3
"""0-prime_game.py"""


def isWinner(x, nums):
    """
    Determines the winner of a game involving prime number removal.
    Args:
        x (int): Number of rounds.
        nums (list of int): List of integers where each n represents a set
        of numbers from 1 to n.
    Returns:
        str("Ben" or "Maria"), None(if no winner)
    """

    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0
    max_num = max(nums)

    primes = [is_prime(i) for i in range(max_num + 1)]

    # Play each round
    for n in nums:
        prime_count = sum(primes[:n + 1])

        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the overall winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def is_prime(n):
    """
    Checks if a number is prime using trial division.
    Args:
        n (int): The number to check for primality.
    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
