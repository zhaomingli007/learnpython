from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Given an array, rotate the array to the right by k steps, where k is non-negative.
        Input: nums = [1,2,3,4,5,6,7], k = 2
        [1,2,3,4,5,6,7] -> [3,2,1,4,5,6,7]->[7,6,1,2,3,4,5]
         
        nums = "----->-->"; k =3
        result = "-->----->"
        reverse "----->-->" we can get "<--<-----"
        reverse "<--" we can get "--><-----"
        reverse "<-----" we can get "-->----->"

        """
        n = len(nums)
        def reverse(i,j):
            while i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        reverse(0, n-1)
        kn = k % n
        reverse(0, kn-1)
        reverse(kn, n-1)

       

if __name__ == '__main__':
    r = Solution()
    nums = [-1]
    r.rotate(nums, 2)
    print(nums)
    
            
        
        
