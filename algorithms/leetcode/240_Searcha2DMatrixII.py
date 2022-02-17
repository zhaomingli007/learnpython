from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        def get_val(start, mid, is_hor):
            if is_hor:
                return matrix[start][mid]
            else:
                return matrix[mid][start]

        def bi_search(start, is_hor):
            lo = start
            hi = n-1 if is_hor else m-1
            while lo <= hi:
                mid = (lo+hi)//2
                if target < get_val(start, mid, is_hor):
                    hi = mid-1
                elif target > get_val(start, mid, is_hor):
                    lo = mid+1
                else:  # find the target
                    return True
            return False

        min_dist = min(m, n)
        for i in range(min_dist):
            is_find = bi_search(i, True) or bi_search(i, False)
            if is_find:
                return True

        return False
