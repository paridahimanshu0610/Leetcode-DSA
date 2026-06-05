class Solution:
    def soFar(self, s, idx1, idx2, dp):
        if idx2 >= idx1:
            dp[idx1][idx2] = 0
            return dp[idx1][idx2]
        
        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2]

        if s[idx1] == s[idx2]:
            dp[idx1][idx2] = self.soFar(s, idx1-1, idx2+1, dp)
        else:
            dp[idx1][idx2] = 1 + min(self.soFar(s, idx1, idx2+1, dp), self.soFar(s, idx1-1, idx2, dp))

        return dp[idx1][idx2]

    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[None]*n for _ in range(n)]

        return self.soFar(s, n-1, 0, dp)