from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
        Input: mat = [[0,0,0],
                      [0,1,0],
                      [1,1,1]]
        Output: [[0,0,0],
                 [0,1,0],
                 [1,2,1]]
        if mat[i][j] == 0, dis: 0
        if  mat[i][j] == 1, check the adjacent recursively, find min(dis)
        """
        m = len(mat)
        n = len(mat[0])
        visited = [[0] * n]*m
        def rec_find(i:int,j:int):
            if mat[i][j] == 0:
                return 0
            if visited[i][j]:
                return 0
            visited[i][j] = 1
            l = mat[i][j] if j-1 < 0 else rec_find(i, j-1)
            r = mat[i][j] if j+1 > n-1  else rec_find(i, j+1)
            u = mat[i][j] if i-1 < 0 else rec_find(i-1, j)
            d = mat[i][j] if i+1 > m-1 else rec_find(i+1, j)
            visited[i][j] = 0
            return min(l, r, u, d) + 1
            
           

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    # visited = [[0] * n]*m
                    mat[i][j] = rec_find(i, j)
        return mat
    
if __name__ == '__main__':
    s = Solution()
    print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
    print(s.updateMatrix(
        [[0, 1, 0], 
         [0, 1, 0], 
         [0, 1, 0], 
         [0, 1, 0], 
         [0, 1, 0]]))
    print(s.updateMatrix(
        [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], 
         [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], 
         [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], 
         [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], 
         [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], 
         [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], 
         [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], 
         [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], 
         [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], 
         [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]))
    
