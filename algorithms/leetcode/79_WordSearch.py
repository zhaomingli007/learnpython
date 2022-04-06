from typing import DefaultDict, List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        adj_ls = DefaultDict(list)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in adj_ls:
                    adj_ls[board[i][j]].append((i, j))
                else:
                    adj_ls[board[i][j]] = [(i, j)]

        dr = [0, -1, 0, 1, 0]

        def dfs(sub, x, y, mem):
            # print(sub,x,y,mem)
            if not sub:
                return True
            exist = False
            for d in range(len(dr)-1):
                r, c = dr[d], dr[d+1]
                if x+r >= 0 and x+r < m and y+c >= 0 and y+c < n and mem[x+r][y+c] == 0 and board[x+r][y+c] == sub[0]:
                    mem[x+r][y+c] = 1
                    exist = dfs(sub[1:], x+r, y+c, mem)
                    # print(x+r, y+c, sub, exist)
                    if exist:
                        break
                    else:
                        # important if not exist reset the marker
                        mem[x+r][y+c] = 0
            return exist

        w = word[0]
        if w in adj_ls:
            for x, y in adj_ls[w]:
                mem = [[0]*n for _ in range(m)]
                mem[x][y] = 1
                ex = dfs(word[1:], x, y, mem)
                if ex:
                    return True
        else:
            return False

        return False
