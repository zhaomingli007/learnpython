from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        "aabcd"
        a, ->abcd
        [a]
             [a, bcd]
             [ab,cd]
        
        aa, -> bcd
        [aa]
        """
        
        n = len(s)
        ans = []
        dp = [[False]*n for _ in range(n) ]
        print(dp)
        cur = [] 
        def dfs(i):
            """
            ans: result list
            cur: curent list with all substr are palindrome
            i: current start position
            dp: memeorise the palindrome of a str from start to end
            """
            nonlocal dp, cur,n 
            
            if i>=n:
                ans.append(cur[:])
            for k in range(i, n):
                #check  s[i] s[k]
                if s[i] == s[k] and (k-i<=2 or dp[i+1][k-1]):
                    dp[i][k]=True
                    cur.append(s[i:k+1])
                    dfs(k+1)
                    cur.pop()
                
        
        dfs(0)
        return ans