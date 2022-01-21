class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").        
        """
        s1map = {}
        n1 = len(s1)
        for c in s1:
            s1map[c] = 1 if c not in s1map else s1map[c]+1
        start = 0
        for i in range(len(s2)):
            new = s2[i]
            if new in s1map:
                s1map[new] -= 1
            if i - start+1 > n1:
                if s2[start] in s1map:
                    s1map[s2[start]] += 1
                start+=1
            #check if the substring is find
            # print(f'start: {start}, i: {i}')
            # print(s1map)
            find = True
            for k in s1map:
                if s1map[k] != 0:
                    find = False
                    break
            if find:
                return True
        return False
        
if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion('hello',"ooolleoooleh"))
    #                               123456789012
    print(s.checkInclusion('ab', "eidbaooo"))
    print(s.checkInclusion('ab', "eidboaoo"))
    print(s.checkInclusion('adc', "dcda"))
    
                
        
        
