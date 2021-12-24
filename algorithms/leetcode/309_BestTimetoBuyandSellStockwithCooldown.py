from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(i):
            """return
            1. max profit when a stock is sold
            2. max profit when a stock is holding
            3. max profit when a stock is cooldown"""
            if(i<0): return -10**9, -10**0, 0
            s, h, c = dp(i-1)
            return h + prices[i], max(h, c - prices[i]), max(c, s)
        return max(dp(len(prices)-1))
