class Solution:
    @cache
    def numBTrees(self, n: int) -> int:
        if n < 1: return 1
        return sum(self.numBTrees(i-1) * self.numBTrees(n-i) for i in range(1, n+1))