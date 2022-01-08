from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        maxSqrLen = 0
        dp = [[0]*cols for _ in range(rows+1)] # dp[i+1][j+1] memorise square less than row i and col j
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1])+1
                    maxSqrLen = max(maxSqrLen, dp[i+1][j+1])
        return maxSqrLen * maxSqrLen
