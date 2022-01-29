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
                
        """
        l = []
        def dp(i, k, p):
            """ 
            Get 1 from i to n until k to 0
            """
            if k == 0:
                l.append(p[:])
            for j in range(i, n+1):
                p.append(j)
                dp(j+1, k-1, p)
                p.pop()
        dp(1, k, [])
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.combine(5,3))
    
