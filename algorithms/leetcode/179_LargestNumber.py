from functools import cmp_to_key
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Input: nums = [3,30,34,5,9]
        
        [3,30,34,5,9,78,72,74186,79]
    
        2=>
        9:[]
        5:[]
        7:[null,8,2,9,4186]
        3:[4,0,null]
        
        3=>
        for 7->  8,2,9,4186
            8:[]
            2:[]
            9:[]
            4:[186] stop
            =>7:[9,8,null,4186,2]
        for 3:
            [4,null,0]
        
        4=>
        9:[]
        5:[]
        7:[9,8,null,4186,2]
        3:[4,null,0]
        
        5=>
        9,5,79,78,7,74186,72,34,3,30
        
                       
        
        Output: "9534330"        
        """
        def cmpr(k1, k2):
            return 1 if k1+k2 <  k2+k1 else -1 #str comparen lexicographical
        
        
        la=sorted(map(str,nums), key=cmp_to_key(cmpr))
        la = ''.join(la)
        return '0' if la[0] == '0' else la
            
            
            
            
        