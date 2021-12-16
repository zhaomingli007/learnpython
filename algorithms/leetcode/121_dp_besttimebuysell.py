from typing import List, Tuple


class MaxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(i:int)->Tuple[int, int]:
            """ Return max profit and min price till now"""
            if i<=0:
                return (0, 10**9)
            maxProfSofar, minPriceSofar = dp(i-1)
            return max(maxProfSofar, prices[i]-minPriceSofar), min(minPriceSofar, prices[i]) 
        return dp(len(prices) - 1)[0]

if __name__ == '__main__':
    mp = MaxProfit()
    print(mp.maxProfit([10,4,5,8,1,5,13]))
    