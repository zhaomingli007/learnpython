class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2147483647 # 2**31-1
        MIN = -2147483648 # -2**31 
        HALF_MIN = -1073741824
        
        if dividend == MIN and divisor == -1:
            return MAX
        
        neg = 2
        if dividend > 0:
            neg -= 1
            dividend = -dividend
        if divisor > 0:
            neg -= 1
            divisor = -divisor
        
        quotient = 0
        while divisor >=dividend:
            powOf2 = -1 
            value = divisor
            while value >= HALF_MIN and value + value >= dividend:
                value += value
                powOf2 += powOf2
            quotient += powOf2
            dividend -= value
            
        
        return -quotient if neg != 1 else quotient