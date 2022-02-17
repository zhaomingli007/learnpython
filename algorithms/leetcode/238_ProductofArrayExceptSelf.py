class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [1, 2, 3, 4]
                       1, 2, 6,24
                      24,24,12, 4
                      24,12, 8, 6]
        Output: [24,12,8,6]
        [1,2,3,4]
         1: 2*3*4
         2: 3*1*4
         3: 4*1*2
         4: 1*2*3
         
         
        """
        if len(nums) <= 1:
            return nums

        n = len(nums)
        tmp1 = [1]*n
        for i in range(n):
            if i >= 1:
                tmp1[i] = tmp1[i-1] * nums[i]
            else:
                tmp1[0] = nums[0]
        # print(tmp1)
        t2 = 1
        ans = [0]*n
        for i in range(n-1, -1, -1):
            if i == 0:
                ans[i] = t2
            elif i == n-1:
                ans[i] = tmp1[i-1]
            else:
                ans[i] = tmp1[i-1] * t2
            t2 = nums[i] if i == n-1 else nums[i]*t2
            # print(t2)

        return ans
