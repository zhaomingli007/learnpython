from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
        """
        

        m = len(board)
        n = len(board[0])

        d = [0,-1,0,1,0]
        
        def sur_O(i, j, mark):
            is_rim = 0
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                # print('rim', i, j)
                return 1
            mark.add((i, j))
            # print(mark)   
            for k in range(len(d)-1):
                x = i+d[k]
                y = j+d[k+1]
                # print(x,y)
                if x>=0 and x<m and y>=0 and y<n:
                    if board[x][y] == 'O' and (x, y) not in mark:
                        is_rim = sur_O(x, y, mark)
                        if is_rim == 1:
                            return 1
            return is_rim
        
        for i in range(m):
            for j in range(n):
                mark = set()
                if board[i][j] == 'O':
                    is_rim = sur_O(i,j, mark)
                    if is_rim == 0:
                        #Flip
                        # print('flip', mark)
                        for kv in mark:
                            x, y = kv
                            board[x][y] = 'X'
                