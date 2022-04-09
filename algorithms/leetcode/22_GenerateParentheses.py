from ast import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        ["((()))","(()())","(())()","()(())","()()()"]
        """
        res = []

        def bt(cur, l, r):
            if len(cur) == 2*n:
                res.append(''.join(cur))
            if l < n:
                cur.append('(')
                bt(cur, l+1, r)
                cur.pop()
                
            if r<l:
                cur.append(')')
                bt(cur,l, r+1)
                cur.pop()
                
        bt([],0,0)

        return res
            
