class Solution:
    def numSquares(self, n: int) -> int:
        """
        Given an integer n, return the least number of perfect square numbers that sum to n.

        Example 1:

        Input: n = 12
        Output: 3
        Explanation: 12 = 4 + 4 + 4.
        Example 2:

        Input: n = 13
        Output: 2
        Explanation: 13 = 4 + 9.  
        min()
                                                                               [4, 9]
                                                     [9]            [4,4,4], [4,4,4,1]
                              [4],   [4,4]           [4,4,1],  ...,   [i^2,...], [i^2,...] 
         1, [1,1], ..., [1,...,1],   [1,...,1],      [1,...,1],  ...,   [1,...,1], [1,...,1]
        [1,     2, ...,         1,                    1,  ...,           3,        2]
         1,     2, ...,         4,     8,             9,  ...,          12,        13
        dp[i] = min(i-j)
        dp[0],dp[1], dp[2] = 0,0,2
        """
        perf_sqr = {}
        for i in range(1, n+1):
            perf_sqr[i*i]=1
            

        dp =[i for i in range( n + 1)]
        dp[0], dp[1] = 1, 1
        print(dp)
        for i in range(2, n+1):
            if i in perf_sqr:
                dp[i] = 1
            else:
                for j in range(2, i+1):
                    dp[i] = min(dp[i],dp[j] + dp[i-j])
        print(dp)
        return dp[-1]
    
    
    def numSquares2(self, n: int)->int:
        """
        dp[i]: min number of perfect squares that make up to i, 
        example: 13 = 4 + 9
        dp[i] = dp[i-j*j] + 1, j*j < i
        min()
                                              dp[4-4]+1,
             dp[1-1]+1, dp[2-1]+1, dp[3-1]+1, dp[4-1]+1,
        dp[ 0,       1,         2,         3,         1]
            0,       1,         2,         3,         4 
        
        """
        dp = [0]+[n+1] * n
        for i in range(1, n+1):
            j = 1
            while j*j <=i:
                dp[i]=min(dp[i],dp[i-j*j]+1)
                j+=1
        print(dp)
        return dp[-1]
        
    
if __name__ == '__main__':
    s = Solution()
    print(s.numSquares2(13))
    
