class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 1
        if s[0] == '0': return 0
        ans = self.numDecodings(s[1:])
        if len(s)>1 and (s[0] == '1' or (s[0] =='2' and s[1]<='6')):
            ans += self.numDecodings(s[2:])
        return ans

if __name__ == '__main__':
    s = Solution()
    r = s.numDecodings('10238712')
    print(r)
    
