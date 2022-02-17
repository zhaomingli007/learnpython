from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        00 dead to dead 0
        10 dead to live 2
        01 live to dead 1
        11 live to live 3
        """
        m, n = len(board), len(board[0])

        def get_lives(i, j):
            n_lives = 0
            state = [-1, -1, 0, -1, 1, 0, 1, 1, -1]
            for s in range(len(state)-1):
                r = i+state[s]
                c = j+state[s+1]
                if r > -1 and r < m and c > -1 and c < n:
                    n_lives += board[r][c] % 2
            return n_lives

        for i in range(m):
            for j in range(n):
                lives = get_lives(i, j)
                if board[i][j] == 1:  # current live
                    if lives < 2 or lives > 3:
                        board[i][j] = 1
                    elif lives == 2 or lives == 3:
                        board[i][j] = 3
                else:  # current dead
                    if lives == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] // 2



if __name__ == '__main__':
    s = Solution()
    board = [[0, 1, 0],
             [0, 0, 1],
             [1, 1, 1],
             [0, 0, 0]]
    s.gameOfLife(board)
    print(board)
    
