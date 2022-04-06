from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        is_col_zr = False
        is_row_zr = False
        for i in range(m):
            if matrix[i][0] == 0:
                is_col_zr = True

            for j in range(n):
                if i == 0 and matrix[0][j] == 0:
                    is_row_zr = True
                    # print(matrix[0])
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # print(matrix, is_row_zr, is_row_zr)
        if is_row_zr:
            for k in range(n):
                matrix[0][k] = 0
        if is_col_zr:
            for k in range(m):
                matrix[k][0] = 0
        # print(matrix)
