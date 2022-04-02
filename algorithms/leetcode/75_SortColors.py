from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Input: nums = [2,0,2,1,1,0]
                       i.        j
                      [0,0,1,1,,1,1,2]
                          i.   j   k

                                                                          
        Output: [0,0,1,1,2,2]        
        """
        n = len(nums)
        i0,i1,i2= 0,0, n-1
        
        while i1 <= i2:
            if nums[i1] == 0:
                nums[i0], nums[i1] = nums[i1], nums[i0]
                i0+=1
            elif nums[i1] == 1:
                i1+=1
            else:
                nums[i1], nums[i2] = nums[i2],nums[i1]
                i2-=1
            if i1<i0:
                i1+=1
            # print(nums, i0,i1,i2)

        