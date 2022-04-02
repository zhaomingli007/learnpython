class Solution:
    def countAndSay(self, n: int) -> str:
        """
        3322251
        
        """
        
        def say(s):
            
            if s == '':
                return '1'
            i, n =0, len(s)
            # print(s)
            ans = ''
            for j in range(1, n):
                if s[j] != s[j-1]:
                    c = str(j-i)
                    ans+=(c+s[i])
                    i = j
            ans+=(str(n-i)+s[i])
            # print('ans', ans)
            return ans
            
        k = ''
        for _ in range(n):
            k = say(k)
        return k
            
            
            
            