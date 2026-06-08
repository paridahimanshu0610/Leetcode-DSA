class Solution:
    def soFar(self, s, t, idx1, idx2, dp):
        if idx1 < 0 or idx2 < 0:
            return 0

        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2]

        if s[idx1] == t[idx2]:
            dp[idx1][idx2] = 1 + self.soFar(s, t, idx1-1, idx2-1, dp)
        else:
            dp[idx1][idx2] = max(self.soFar(s, t, idx1-1, idx2, dp), self.soFar(s, t, idx1, idx2-1, dp))

        return dp[idx1][idx2]
    
    def getAllLCS(self, s, t, idx1, idx2, dp):
        if idx2 < 0:
            return 1
        elif idx1 < 0:
            return 0

        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2]

        if s[idx1] == t[idx2]:
            dp[idx1][idx2] = self.getAllLCS(s, t, idx1-1, idx2-1, dp) + self.getAllLCS(s, t, idx1-1, idx2, dp)
        else:
            dp[idx1][idx2] = self.getAllLCS(s, t, idx1-1, idx2, dp)

        return dp[idx1][idx2]

    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp = [[None]*n for _ in range(m)]

        # self.soFar(s, t, m-1, n-1, dp)
        # maxLen = dp[m-1][n-1]

        # if maxLen < n:
        #     return 0

        dp = [[None]*n for _ in range(m)]
        self.getAllLCS(s, t, m-1, n-1, dp)

        return dp[m-1][n-1]