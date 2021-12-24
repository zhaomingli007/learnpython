from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        def dp(i):
            """  value[i]+i + value[j]-j, i<=j 
            return maxScore from 0 to i
            return max value of value[i]+i
            """
            if i < 0: return -10**9, -10**9
            maxScore, maxPastValue = dp(i-1)
            return max(maxScore, maxPastValue + values[i] - i), max(maxPastValue, values[i] -i)
        return dp(len(values)-1)