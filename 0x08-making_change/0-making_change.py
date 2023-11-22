#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """Finds the minimum number of coins needed to reach total"""
    dp = [float("inf") for i in range(total + 1)]

    dp[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] != float("inf"):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float("inf") else -1
