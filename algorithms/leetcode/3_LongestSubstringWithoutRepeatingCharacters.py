class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Input: s = "pwwkew"
        Output: 3 
        2
        3
        "pwwkew"   
        """
        n =len(s)
        if n == 0: 
            return 0
        max = 0
        for i in range(n):
            cur_set = set()
            print('{0} loop'.format(i))
            for j in range(i, n):
                if s[j] in cur_set:
                    break
                else:
                    cur_set.add(s[j])
            cur_len = len(cur_set)
            max = cur_len if cur_len > max else max
            print(cur_set)
        return max
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        'xxzqixaxq'
                 i
               j only update when used[i] exist and j < used[c], like 'q' in this case should be updated to a smaller index
        {x:5,z:2,q:3,i:4,a:6}
        """
        j = m = 0
        used = {}
        for i, c in enumerate(s):
            if c in used and j<=used[c]:
                j = used[c] + 1
            else: 
                m = max(m, i-j+1)
            used[i] = c
                
if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring2('xxzqi'))
    
