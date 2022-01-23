from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        You are given an m x n grid where each cell can have one of three values:
        0 representing an empty cell,
        1 representing a fresh orange, or
        2 representing a rotten orange.
        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
        Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.        
        Input: grid = [
            [2,1,1],
            [1,1,0],
            [0,1,1]]
        Output: 4
        q: 1: [(0,1)], 2: [(0,1),(0,1)], 3:[(0,2),(1,1)], 4:[(2,1)], 5:[(2,2)] 
        
        [[2,1,1],
         [0,1,1],
         [1,0,1]]
        """
        m = len(grid)
        n = len(grid[0])
        q = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        dir = [0, 1, -1,0, 0]
        while len(q) > 0:
            i, j = q.pop(0)
            for d in range(4):
                if i-1 > 0 and grid[i-1]>0:
                    grid[i-1][j] = 2
                    q.append((i-1, j))
                if i+1 > m-1 and grid[i+1]>0:
                    grid[i+1][j] = 2
                    q.append((i+1, j))
            
            