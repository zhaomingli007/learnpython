from typing import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # delta
        def impact(passed, total):
            return (passed+1)/(total+1) - passed / total
        maxHeap = []
        for a, b in classes:
            a, b = a*1.0, b*1.0
            maxHeap.append((-impact(a, b), a, b))
        heapq.heapify(maxHeap)

        for _ in extraStudents:
            _, a, b = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-impact(a+1, b+1), a, b))
        return sum(a / b for _, a, b in maxHeap / len(classes))
