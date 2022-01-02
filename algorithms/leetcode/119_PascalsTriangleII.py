from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] # when row index is 0
        # from row row index 1 to rowIndex
        for i in range(1, rowIndex + 1):
            tmp = [1] * (i+1)
            for j in range(1, i):
                tmp[j] = ans[j-1] + ans[j]
            ans = tmp
        return ans