from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:
            i - k <= r <= i + k,
            j - k <= c <= j + k, and
            (r, c) is a valid position in the matrix.
            Range sum: rangeSum[i+1][j+1] =  rangeSum[i][j+1] + rangeSum[i+1][j]    -   rangeSum[i][j]   + mat[i][j]
            Block sum: 
            +---------------+   +--------------+   +---------------+   +--------------+   +--------------+
            |               |   |         |    |   |   |           |   |         |    |   |   |          |
            |   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |          |
            |   +------+    |   |         |    |   |   |           |   +---------+    |   +---+          |
            |   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)    |
            |   |      |    |   |         |    |   |   |           |   |              |   |              |
            |   +------+    |   +---------+    |   +---+           |   |              |   |              |
            |        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |              |
            +---------------+   +--------------+   +---------------+   +--------------+   +--------------+            
        """
        m, n = len(mat), len(mat[0])
        # Initialize range sum matrix
        range_sum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                range_sum[i+1][j+1] = range_sum[i][j+1]+range_sum[i+1][j] - range_sum[i][j] + mat[i][j]
        #calculate block sum
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, r2, c1, c2 = max(0, i-k), max(m,i+k+1), max(0, j-k), max(n, j+k+1)
                ans[i][j]=range_sum[r2][c2] - range_sum[r2][c1]-range_sum[r1][c2] +mat[r1][c1]
        return ans