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
        sec = 0
        q1 , q2 = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q1.append((i, j))
        dir = [0, -1, 0, 1, 0] # up: (0, -1), left: (-1, 0), down: (0, 1), right: (1, 0)
        while len(q1) > 0:
            i, j = q1.pop(0)
            # print('i: ', i, ',j: ', j)
            for d in range(4):
                r = i + dir[d]
                c = j + dir[d+1]
                if -1 < r < m and -1 < c < n and grid[r][c] ==1:
                    # print('r: ', r, ',c: ', c)
                    grid[r][c] = 2
                    q2.append((r, c))
            if len(q1) == 0:
                if len(q2)>0:
                    sec += 1
                q1, q2 = q2, []
                
        print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return sec
            
if __name__ == '__main__':
    s = Solution()
    print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(s.orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]))
    
 
