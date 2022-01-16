
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        coins = [1,2,5], amount = 11
                min                                           
                                                             dp[5-5]+1,
            min(dp[i-c]+1), dp[2-2]+1, dp[3-2]+1, dp[4-2]+1, dp[5-2]+1,
                 dp[1-1]+1, dp[2-1]+1, dp[3-1]+1, dp[4-1]+1, dp[5-1]+1,
        dp[i]:[0,        1,         1,         2,         2,         3,                      ]
               0,        1,         2,         3,         4,         1,     6, 7, 8, 9, 10, 11
        """
        dp = [0] + [float('inf') for _ in range(amount)]
        for i in range(1, amount+1):
            for c in coins:
                if i - c>=0:
                    dp[i] = min(dp[i], dp[i-c]+1)

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1,2,5],11))
    print(s.coinChange([2],3))
    print(s.coinChange([1],0))
    
