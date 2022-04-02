from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        dr = [0,1,0,-1,0 ]
        
        
        m, n = len(matrix), len(matrix[0])
        i,j = 0,0
       
        ans = []

        d = 0
        while True:
            is_end = False
            
            ans.append(matrix[i][j])
            matrix[i][j] = math.inf
            d = d % 4
            n_i, n_j = i+dr[d], j+dr[d+1]
            
            turn_cnt = 0
            while n_i< 0 or n_i>m-1 or n_j<0 or n_j> n-1 or matrix[n_i][n_j] == math.inf:
                d = (d+1) % 4
                turn_cnt += 1
                if turn_cnt==2:
                    is_end = True     
                    break
                # print('change', i, j, d)
                n_i, n_j = i+dr[d], j+dr[d+1]
               
            # print(matrix)
            if is_end:
                break
            i, j = n_i, n_j
            
        return ans
           
        
        