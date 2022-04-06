from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2 + n % 2):
            len_i = n-i*2 - 1
            # print(len_i)
            for j in range(len_i):
                r1, c1 = i, i+j
                r2, c2 = i+j, i+len_i
                r3, c3 = i+len_i, i+len_i-j
                r4, c4 = i+len_i-j, i
                # print(matrix[r1][c1], matrix[r2][c2], matrix[r3][c3], matrix[r4][c4])
                tmp = matrix[r1][c1]
                matrix[r1][c1], matrix[r4][c4],  matrix[r3][c3] = matrix[r4][c4], matrix[r3][c3],  matrix[r2][c2]
                matrix[r2][c2] = tmp
