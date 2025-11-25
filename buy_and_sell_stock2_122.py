# 122. Best Time to Buy and Sell Stock II
# Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, n = 0, len(prices) - 1
        low = prices[0]
        high = prices[0]
        profit = 0

        while i < n:
            while i < n and prices[i] >= prices[i + 1]:
                i += 1
            low = prices[i]

            while i < n and prices[i] <= prices[i + 1]:
                i += 1
            high = prices[i]

            profit += high - low

        return profit