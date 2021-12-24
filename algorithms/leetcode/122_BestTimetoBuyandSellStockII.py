from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(i):
            """return 
            1. max profit till i, hold no stocks, can buy
            2. max current balance till i ( initially no balance and by a stock will make negative balance), hold stocks can sell"""
            if i<0: return 0, -10**9
            p, b = dp(i-1)
            return max(p, b + prices[i]), max(b, p - prices[i])
        return dp(len(prices)-1)[0]