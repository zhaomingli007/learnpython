class Solution:
    # "babad"-> "bab" or "aba"
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)] # initialize dp array, dp[i][j] == 1 if start from i to j is a palindrome
        for i in range(n): #
            dp[i][i] = True
        long_palind_start, long_palind_len = 0, 1
        for end in range(0, n):
            for start in range(end-1,-1,-1):
                if s[start] == s[end]:
                    if end -start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        palindrome_len = end - start + 1
                        if long_palind_len < palindrome_len :
                            long_palind_len = palindrome_len
                            long_palind_start = start
        return s[long_palind_start:long_palind_start+long_palind_len]
                                                                                                                        