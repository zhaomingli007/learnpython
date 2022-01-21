from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        Output: 6                
        """
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0
            if grid[r][c] == 1:
                grid[r][c] +=1
                #right, left, up, down
                return dfs(r, c+1)+dfs(r, c-1)+dfs(r-1, c)+dfs(r+1, c) +1
            if grid[r][c] == 0:
                grid[r][c] -=1
            return 0
        
        # for reach point
        area = 0
        for i in range(m):
            for j in range(n):
                area = max(area, dfs(i, j))
        return area

if __name__ == '__main__':
    s = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(s.maxAreaOfIsland(grid))
    
