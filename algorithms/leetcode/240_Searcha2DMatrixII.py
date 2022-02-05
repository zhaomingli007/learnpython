from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        def search(r_left,r_right, c_top, c_bottom):
            if r_left>r_right or c_top > c_bottom:
                return r_left,r_right, c_top,c_bottom
            r_mid = r_left + (r_right-r_left) // 2
            c_mid = c_top + (c_bottom-c_top) // 2
            if target == matrix[r_mid][c_mid]:
                return r_mid,r_mid, c_mid,c_mid
            elif target < matrix[r_mid][c_mid]: #
                r_right = r_mid-1
                c_bottom = c_mid-1
            else:
                r_left = r_mid+1
                c_top = c_mid+1
            return search(r_left, r_right, c_top, c_bottom)
        
        l,r, t,b = search(0, m-1, 0, n-1)
        for i in (l,r):
             for c in matrix[i]:
                if target == c:
                    return True
        for j in (t,b):
            for i in range(m):
                if target == matrix[i][j]:
                    return True
        return False
        
if __name__ == '__main__':
    s = Solution()
    # print(s.searchMatrix([[1,4],[2,5]],1))
    # print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
    # print(s.searchMatrix([[1,2,3,4,5],
    #                       [6,7,8,9,10],
    #                       [11,12,13,14,15],
    #                       [16,17,18,19,20],
    #                       [21,22,23,24,25]],15))
    # print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20))
    print(s.searchMatrix([[1,  4, 7,11,15,40],
                          [2,  5, 8,12,19,50],
                          [3,  6, 9,16,22,60],
                          [10,13,14,17,24,70],
                          [18,21,23,26,30,80]],18))
    # print(s.searchMatrix([[1,2,3,4,5],
    #                       [6,7,8,9,10],
    #                       [11,12,13,14,15],
    #                       [16,17,18,19,20],
    #                       [21,22,23,24,25]],5))
    
    