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
        """
        m = len(mat)
        n = len(mat[0])

        def update(x, y, h, v):
            ud = float('inf') if x+h < 0 or x+h > m-1 else mat[x+h][y]
            lr =  float('inf') if y+v < 0 or y+v > n-1 else mat[x][y+v]
            if h<0: # top down
                mat[x][y] = min(ud, lr)+1
            else:
                mat[x][y] = min(mat[x][y], min(ud, lr)+1)
        def scan(bu):     
            for i in range(m):
                for j in range(n):
                    if bu<0: #top down, left -> right
                        x, y = i, j
                    else: #bottom up, right -> left
                        x, y = m - i -1, n - j -1
                    if mat[x][y] > 0:
                        update(x, y, bu, bu)
                
        scan(-1) #top down
        scan(1) #bottom up
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
    
