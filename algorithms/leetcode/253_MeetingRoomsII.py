import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        [[0,30],[5,10],[15,20]]
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
                   5,6,7,8,9,10             15,16,17,18,19,20
                                            
        """
        
#         m = len(intervals)
#         mrange = -1
#         for i in range(m):
#             mrange = max(mrange, intervals[i][1])
        
#         max_room = 1
#         for i in range(mrange+1):
#             r_max = 0
#             for j in range(m):
#                 if intervals[j][0]< i <= intervals[j][1]:
#                     r_max+=1
#             max_room = max(max_room, r_max)
#         return max_room
        #use priority queue 
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[0])
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for i in intervals[1:]:
            if rooms[0] <= i[0]: #free
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])
        return len(rooms)