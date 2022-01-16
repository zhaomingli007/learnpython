from typing import List


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        """
        Return number of combinations that make up that amount
            Input: amount = 5, coins = [1,2,5]
            Output: 4
            Explanation: there are four ways to make up the amount:
            5=5
            5=2+2+1
            5=2+1+1+1
            5=1+1+1+1+1
        dp[i] number of ways to make up i
        for c in [1, 2, 5], amount: 5
                                                         [5],
                                          [2,2],     [2,2,1],
                        [2],   [2,1],   [2,1,1],   [2,1,1,1],
                   1, [1,1], [1,1,1], [1,1,1,1], [1,1,1,1,1],
        dp[i]: [1, 1,     2,    2,            3,           4,     ]
                   1,     2,    3,            4,           5,
        amount: 5, dp[5] = max(dp[5-1]=3+1, dp[5-2]=2+1, dp[5-5]=1+1)
        amount: 4, dp[4] = dp[4-1] + dp[4-2] = 4
        amount: 3, dp[3] = dp[3-1] +  dp[3-2], 2+1 = 3 # duplicated, should be 2
        amount: 2, dp[2] = dp[2-1] +  dp[2-2], 1+1 = 2
        amount: 1, dp[1] = dp[1-1] = 1
        dp[0] = 1
        
        for c in [1, 2, 5], amount: 5  
        coin 1:
        dp: [1,1,1,1...]
        coin 2:
        amount start from 2:
                   dp[2]+=dp[2-2], dp[3]+=dp[3-2],  dp[4]+=dp[4-2], dp[5]+=dp[5-2],
        dp: [1, 1,              2,              2,               3,              3,]
             0, 1,              2,              3,               4,              5 
        coin 5:
        amount start from 5:
                                                                    , dp[5]+=dp[5-5],
        dp: [1, 1,              2,              2,               3,              4,]
             0, 1,              2,              3,               4,              5 

        """
        dp = [1] + [0]*amount
        for c in coins:
            for i in range(c, amount+1):
                    dp[i] += dp[i-c]
        return dp[-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.change(5, [1,2,5]))
    
