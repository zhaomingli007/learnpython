# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        graph = [[1,1,0],
                1[0,1,0],
                 [1,1,1]]
        output: 1
        Input: graph = [[1,0,1],
                        [1,1,0],
                        [0,1,1]]
                        
        solution: exception diagnal all columns of a row are 0
        """
        for i in range(n):
            k = 0 # is celebrity
            for j in range(n):
                if i!=j and (not knows(j,i) or knows(i,j)):
                    k = 1
                    break
            if k == 0:
                return i
                    
            
        return -1
            