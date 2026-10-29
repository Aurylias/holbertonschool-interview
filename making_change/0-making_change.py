#!/usr/bin/python3
"""Determine the fewest number of coin needed to meet a given amout"""


def makeChange(coins, total):
    """Determine the fewest coin needed to reach total from a list of coin"""
    if total <= 0:
        return 0

    coins = sorted(set(coins))
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin > amount:
                break
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != float('inf') else -1

if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
