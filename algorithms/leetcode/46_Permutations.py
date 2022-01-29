from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Input: nums = [1,2,3]
        Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]    
        1, [2,3]
            2,[3]
            3,[2]
        2, [1,3]
        3, [2,1]
         
        """
        n = len(nums)
        l = []
        def bt(sub, p): # handle sub list start from i to n-1
            if len(p) == n:
                l.append(p[:])
            for j in range(len(sub)):
                p.append(sub[j])
                sub[j], sub[0] = sub[0], sub[j]
                bt(sub[1:],p)
                p.pop()
                
        bt(nums,[])
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
    
