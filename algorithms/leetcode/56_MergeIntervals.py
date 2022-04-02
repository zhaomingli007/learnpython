from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [[1,3],[2,6],[8,10],[15,18]]
        
        """
        intervals.sort(key=lambda p: p[0])
        n = len(intervals)
        if n <=1:
            return intervals
        
        merged = []
        for i in range(n-1):
            if intervals[i][1] >= intervals[i+1][0]:
                mp = (intervals[i][0], max(intervals[i+1][1],intervals[i][1]))
                intervals[i+1] = mp
                
            else:                
                merged.append(intervals[i])

                
        merged.append(intervals[n-1])
        return merged