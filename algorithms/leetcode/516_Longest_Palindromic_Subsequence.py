class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        maxLen = 1
        for j in range(n):
            for i in range(j-1, -1, -1):
                if i<j:
                    dp[i][j] = 2 + dp[i+1][j-1] if s[i] == s[j] else max(dp[i][j-1],dp[i+1][j])
                    if maxLen < dp[i][j]:
                        maxLen = dp[i][j]
        return maxLen