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
    
    def maxProduct2(self, nums:List[List]) -> int:
        def dp(i):
            """ return max and min sub array project until i"""
            if i ==  0: return nums[i], nums[i]
            maxP, minP = dp(i-1)
            if nums[i] < 0:
                maxP, minP = minP, maxP
            return max(nums[i], nums[i] * maxP), min(nums[i], nums[i]*minP)
        return max(dp(i)[1] for i in range(len(nums)))
        

            
    
if __name__ == '__main__':
    maxProd = Solution()
    prod = maxProd.maxProduct([2,3,-2,4])
    print(prod)
    
