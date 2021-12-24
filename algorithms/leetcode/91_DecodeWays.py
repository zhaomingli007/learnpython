class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        def dp(i):
            """return 
            number of ways decoding till i-1 and i-2"""

            if i == 0 and s[i] == '0':
                return 0, 0
            if i == 0:
                return 0, 1
            pre2, pre = dp(i-1)
            if s[i] == '0':
                return pre, pre
            elif int(s[i-1:i]) <= 26:
                return pre, max(1 + pre, 2+pre2)
            else: return pre, pre+1
        return max(dp(i)[1] for i in range(len(s)))

if __name__ == '__main__':
    s = Solution()
    r = s.numDecodings('12')
    print(r)
    
