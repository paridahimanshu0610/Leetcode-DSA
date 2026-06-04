class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0]*n

        i = 0
        while i < n:
            if s[0] == s[n-1-i]:
                break
            i += 1
        while i < n:
            dp[i] = 1
            i += 1

        for idx1 in range(1, n):
            temp = [0]*n
            for idx2 in range(n):
                if s[idx1] == s[n-1-idx2]:
                    temp[idx2] = (1 + dp[idx2-1]) if (idx2-1) >= 0 else 1
                else:
                    temp[idx2] = max(temp[idx2-1], dp[idx2])
            dp = temp

        return dp[n-1] 