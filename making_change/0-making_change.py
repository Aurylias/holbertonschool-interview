#!/usr/bin/python3
"""Determine the fewest number of coin needed to meet a given amout"""


def makeChange(coins, total):
    """Determine the fewest coin needed to reach total from a list of coin"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        if total <= 0:
            break

        coin_count += total // coin
        total %= coin

    if total != 0:
        return -1

    return coin_count


if __name__ == '__main__':
    pass
