from typing import List


class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sum_range = [[0]*n for _ in range(m+1)]
        for r in range(m):
            for c in range(n):
                self.sum_range[r+1][c+1] = self.sum_range[r+1][c] + self.sum_range[r][c+1] - self.sum_range[r][c] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1+1,col1+1,row2+1,col2+1
        return self.sum_range[row2][col2] - self.sum_range[row2][col1-1] - self.sum_range[row1-1][col2] + self.sum_range[row1-1][col1-1]
        