class Solution:
    def integerBreak(self, n: int) -> int:
        """
        Input: n = 10
        Output: 36
        Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36  
        dp[i]: maximum product till i      
                                       5*1
                                       4*2
                                       4*1
                                       3*3
                                       3*2
                                       3*1 
                            4*1,       2*4
                            3*2,       2*3*1
                       3*1, 2*3,       2*2*2
                       2*2, 2*2*1,     2*2*1
                  2*1, 2*1, 2*1*1*1,   2*1
             1*1, 1*1, 1*1, 1*1*1*1*1, 1*1
        dp[]: [1,   2,   4,   6,         9,         ]
               2,   3,   4,   5,        6
        
        dp[0]=dp[1]=1
        dp[6] = 2+4, max(2, dp[2]) * max(4,  dp[4]) = 8
              = 3+3, max(3, dp[3]) * max(3, dp[3]) = 9
              = 5+1, max(5, dp[5]) * 1 = 6
        """
        dp = [1] * (n+1)
        for i in range(2, n+1):
            for j in range(1,i):
                dp[i]=max(max(j, dp[j]) * max(i-j, dp[i-j]), dp[i])
        print(dp)
        return dp[-1]
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.integerBreak(10))
    
    
