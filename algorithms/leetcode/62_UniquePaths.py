class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(i,j):
            if i<0 or j<0: return 0
            if i == 1 and j == 1: return 1
            return dp(i-1,j) + dp(i,j-1)
        return dp(m, n)
    
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                #move right
                if j-1>=0:
                    dp[i][j]+=dp[i][j-1]
                #move down
                if i-1 >=0:
                    dp[i][j]+=dp[i-1][j]
        
        return dp[i][j]
        