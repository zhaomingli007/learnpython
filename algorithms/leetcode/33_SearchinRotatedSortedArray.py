class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [4,5,6,7, 0,1,2], target = 0
       
        """
        def find(i, j):
            while i<=j:
                m = (i+j)//2
                if nums[m] == target:
                    return m
                elif  nums[m] >= nums[i]: # mid > start
                    if target >= nums[i] and target < nums[m]:
                        j = m-1
                    else:
                        i = m +1
                       
                else:                    # mid < start
                    if target < nums[m]:
                        j = m - 1
                    elif target >= nums[i]:
                        j = m -1
                    else:
                        i = m + 1
                   
            return -1
       
        return find(0, len(nums) - 1)

