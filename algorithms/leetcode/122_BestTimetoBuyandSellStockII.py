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


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [7,1,5,3,6,4]
       
        """
        n = len(prices)
        # (hold stock can sell - max money in hand, no stock can buy-max profit)
        dp = [(-prices[0], 0)] * n

        for i in range(1, n):
            max_mny, mx_prf = dp[i-1]
            dp[i] = (max(max_mny, mx_prf-prices[i]),
                     max(mx_prf, max_mny+prices[i]))
        return dp[-1][1]
