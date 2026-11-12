#!/usr/env/python3
"""
A game where the players take turns and remove a prime number and it's 
multiples from the given set. The player that cannot make a move loses the game
"""

def crible_eratosthene(max_n):
    """Use the Ératosthène algorithm to find all prime number in a range"""
    prime = [True] * (max_n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, max_n + 1, i):
                prime[j] = False

    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(max_n + 1):
        if prime[i]:
            count += 1
        prime_count[i] = count

    return prime_count
    

def isWinner(x, nums):
    """
    Return who wins based on the given set and round.

    x: The number of round of the game.
    nums: The set of numbers used for the game.
    """

    if not nums or x < 1:
        return None

    max_n = max(nums)
    if max_n < 2:
        return 'Ben'

    prime_count = crible_eratosthene(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"

    return None

