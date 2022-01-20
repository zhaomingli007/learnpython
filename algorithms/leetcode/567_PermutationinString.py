class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").        

        s1='adc'
            {a:1, d:1, c:1}
            n = 3
            tmp: {c:1, d:1,a:1}
        s2='dcda'
             i j
        
        'ab'
        'eidbaooo'
              i
            j
        """
        
        s1m = {}
        for c in s1:
           if c in s1m:
               s1m[c] += 1
           else:
               s1m[c] = 1
        print(s1m)
        start = 0
        tmp = {}
        for i in range(len(s2)):
            print(f'start {start}, i: {i} ')
            
            c = s2[i]
            if c in s1m:
                if c not in tmp:
                    tmp[c] = 1
                elif tmp[c]< s1m[c]:
                        tmp[c] += 1
                else:
                    start += 1
                    # tmp[c] -=1
            else:
                start = i+1
                tmp = {}
            print(tmp)
            if i-start+1 == len(s1):
                return True
        return False
if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion('hello',"ooolleoooleh"))
    # print(s.checkInclusion('ab', "eidbaooo"))
    # print(s.checkInclusion('adc', "dcda"))
    
                
        
        
