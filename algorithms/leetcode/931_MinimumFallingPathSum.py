from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)): # compute min path from 2 row
            for j in range(len(matrix[0])): #compute min path from 1 column
                if j == 0: # when j is first column, then only have two way to fall down
                    matrix[i][j] = min(matrix[i-1][j]+matrix[i][j], matrix[i-1][j+1]+matrix[i][j])
                elif j == len(matrix[0]) - 1: # when j is last column
                    matrix[i][j] = min(matrix[i-1][j]+matrix[i][j], matrix[i-1][j-1]+matrix[i][j])
                else:
                    matrix[i][j] = min(matrix[i-1][j]+matrix[i][j], matrix[i-1][j-1]+matrix[i][j], matrix[i-1][j+1]+matrix[i][j])

        return min(matrix[-1])
                