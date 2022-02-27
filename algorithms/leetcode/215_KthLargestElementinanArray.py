class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        [3,2,3,1,2,4,5,5,6]
        pivot pos: 5
        exchange 0 with 5, 
        [5,2,3,1,2,4,3,5,6]
                     ^
           i=1
           j=1,j+=1
        [5,2,3,1,2,4,3,5,6]
           i
             j
             3<5
        [5,2,3,1,2,4,3,5,6]
           i
               j
               1<5   
        [5,2,3,1,2,4,3,5,6]
           i
                 j
                 2<5  
        [5,2,3,1,2,4,3,5,6]
           i
                     j
                     3<5   
        [5,2,3,1,2,4,3,5,6]
           i
                       j
                       5>=5 , exchange
        [5,5,3,1,2,4,3,2,6]
           i
                       j
        [5,5,3,1,2,4,3,2,6]
             i
                         j, j till end, exange 0 with i
        [5,5,3,1,2,4,3,2,6]
             i
                         j,
        if i == n-1, exchange 0 with i
        else echange 0 with i-1
                                          
        """