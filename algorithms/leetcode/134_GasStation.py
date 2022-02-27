from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #(position, longest can reach, remains)
        n = len(gas)
        
        start_idx = to_tank = cur_tank= 0
        
        for i in range(len(gas)):
            cur_tank+=gas[i]-cost[i]
            to_tank+=gas[i]-cost[i]
            if cur_tank < 0:
                start_idx = i + 1
                cur_tank = 0
        return -1 if to_tank < 0 else start_idx
            
        
            