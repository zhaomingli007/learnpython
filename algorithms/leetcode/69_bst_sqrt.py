class Solution:

    def power(self, x, n):
        """Compute 2^n in O(log(n))"""
        if n == 0:
            return 1
        r = self.power(x, n//2)
        if n % 2 == 0:
            return r*r
        else:
            return x*r*r

    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l+(r-l) // 2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            if x < mid * mid:
                r = mid -1
            else:
                l = mid +1
            
if __name__ == '__main__':
    t = Solution()
    print(t.mySqrt(8))
    
