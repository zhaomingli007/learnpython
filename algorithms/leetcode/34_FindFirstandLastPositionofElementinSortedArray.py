class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def find(i, j):
            while i <= j:
                m = (i+j)//2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    i = m + 1
                else:
                    j = m - 1
                   
            return -1
       
        mid = find(0, n-1)
        if mid == -1:
            return [-1,-1]
        #left
        l , r = mid, mid
        while l-1 >= 0 and nums[l-1] == target :
            l = find(0, l-1)
       
        while r+1 < n  and nums[r+1] == target :
            r = find(r+1, n-1)
        return [l, r]