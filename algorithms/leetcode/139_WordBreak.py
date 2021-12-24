from typing import List


class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
    @__cached__
    def dp(s):
        """
            s = "applepenapple", wordDict = ["apple","pen"]
                      i
        return true if the substring (0 to i) is breakable.
        """
        ws = set(wordDict)
        n  = len(s)
        if not s: return True
        for l in range(1, min(n, 20)+1):
            if s[0:l] in ws and dp(s[l:]): return True

    return dp(s) 
