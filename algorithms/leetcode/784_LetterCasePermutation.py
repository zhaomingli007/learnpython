from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Input: s = "a1b2"
        Output: ["a1b2","a1B2","A1b2","A1B2"]
        'A' -ASCII-> 65
        'a' --> 97
        '0' --> 48
        diff: 32
        
        """
        n = len(s)
        l = []
        def bt(i, p):
            if len(p) == n:
                l.append(''.join(p))
                return
            for j in range(i, n):
                p.append(s[j])
                bt(j+1, p)
                p.pop()
                if s[j].isalpha():
                    p.append(s[j].upper() if ord(s[j])>=97 else s[j].lower())
                    bt(j+1, p)
                    p.pop()
        bt(0, [])
        return l
if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation('a1b2C'))
    
