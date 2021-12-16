from typing import List, Tuple

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = nums[0]
        for n in nums:
            vals = (n, n*currMax, n*currMin)
            currMax, currMin = max(vals), min(vals)
            res  = max(res, currMax)
        return res
    
if __name__ == '__main__':
    maxProd = Solution()
    prod = maxProd.maxProduct([2,3,-2,4])
    print(prod)
    
