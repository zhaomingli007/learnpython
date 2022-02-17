class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        5! = 120
        9*8*7*6*5*4*3*2*1
        [2,5]
        [4,5]
        [6,5]
        [8,5]
        
        [1,10]
        1. check how many 10, +
        2. how many 5
        (n // 10)*5 + (n % 10 )//2
        
        [xxx] 10 of them, have 5 0s
        
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
                ^               ^
    11,12,13,14,15,16,17,18,19, 20
                ^               ^
    21,22,23,24,25,26,27,28,29, 30 (2*25 = 50, 4*50 = 200,  every 25 , +2)
                ^               ^
                *
    31,32,33,34,35,36,37,38,39, 40
                ^               ^                    
    41,42,43,44,45,46,47,48,49, 50 (1*50, 2*50)
                ^               ^ 
                                *
    51,52,53,54,55,56,57,58,59, 60 (2*55 = 110)
                ^                ^
    61,62,63,64,65,66,67,68,69, 70 (2*65 = 130)
                ^                ^
    71,72,73,74,75,76,77,78,79, 80 (2*75 = 150, 4*150 = 600 )
                 ^
                 *
    81,82,83,84,85,86,87,88,89, 90
    ...
    ...,       125, ...             (2*125 = 250, 4*250 =1000, +3 )

    
    
        n/5 + n/25 (2 factors) + n/125 (3 factors) + ...

        """

        ans = 0
#         for i in range(5, n+1, 5):
#             j = i
#             while i % 5 == 0: # find all factors of 5 of number i
#                 ans += 1
#                 j //= 5

        while n > 0:
            n //= 5
            ans += n

        return ans