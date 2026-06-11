class Solution:
    def soFar(self, s1, s2, idx1, idx2, dp):
        if idx1 < 0 or idx2 < 0:
            return 0

        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2]
            
        if s1[idx1] == s2[idx2]:
            dp[idx1][idx2] = 1 + self.soFar(s1, s2, idx1-1, idx2-1, dp)
        else:
            dp[idx1][idx2] = max(self.soFar(s1, s2, idx1, idx2-1, dp), self.soFar(s1, s2, idx1-1, idx2, dp))

        return dp[idx1][idx2]

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[None]*n for _ in range(m)]

        return self.soFar(s1, s2, m-1, n-1, dp)