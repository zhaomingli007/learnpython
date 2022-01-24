from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].        
        Input: n = 4, k = 2
        Output:
        [
            [2,4],
            [3,4],
            [2,3],
            [1,2],
            [1,3],
            [1,4],
        ] 
        0...n: [1,2,3,4], k = 2
        1:(1,2),(1,3),(1,4) 
        2:(2,3),(2,4)
        3:(3,4)
        4:
        k = 3
        1: (1, 2, 3), (1, 3, 4)
        2: (2, 3, 4), (2, 1, 4)
        3: 
        4:
        dp[i][k] from i to n, get k of comb; return a list
        i + dp[i-1][k-1]
        
        """
        pass
