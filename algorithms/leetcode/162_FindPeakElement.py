class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        nums = [1,2,4,3,8,10,5, 6, 7,1,3,5,6,4]
               [1,2,4,3,8,10,5] 6 [7,1,3,5,6,4]
               [1,2,4]3[8,10,5] 6 [7,1]3[5,6,4]
        if nums[mid] is in a descending order, then the peak will be land on left , otherwise it will land on right. util single point left.
               
        """
        def find_peak_rec(l: int, r: int) -> int:
            if l == r:
                return l
            m = (l+r)//2
            # print(l, r, m)
            # on descending order
            if nums[m] > nums[m+1]:
                return find_peak_rec(l, m)
            else:
                return find_peak_rec(m+1, r)
            
        return find_peak_rec(0, len(nums)-1)