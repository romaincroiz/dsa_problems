from typing import List

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""
def max_profit(prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0

    min_price = prices[0]
    profit = 0
    # need to iterate from left to right to ensure we buy before selling
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            if prices[i] - min_price > profit:
                # update the profit to be made if sold on that day
                profit = prices[i] - min_price

    return profit