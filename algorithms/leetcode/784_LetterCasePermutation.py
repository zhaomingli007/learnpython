from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Input: s = "a1b2"
        Output: ["a1b2","a1B2","A1b2","A1B2"]
        """
        n = len(s)
        l = []
        def bt(sub, p):
            if len(p) == n:
                l.append(p)
            for i in range(len(sub)):
                if i 
            
