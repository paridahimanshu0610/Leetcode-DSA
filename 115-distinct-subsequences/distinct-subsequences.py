class Solution:
    def soFar(self, s, t, idx1, idx2, dp):
        if idx2 < 0:
            return 1
        elif idx1 < 0:
            return 0

        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2]

        if s[idx1] == t[idx2]:
            dp[idx1][idx2] = self.soFar(s, t, idx1-1, idx2-1, dp) + self.soFar(s, t, idx1-1, idx2, dp)
        else:
            dp[idx1][idx2] = self.soFar(s, t, idx1-1, idx2, dp)

        return dp[idx1][idx2]

    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp = [[None]*n for _ in range(m)]
        dp = [0]*(n+1)
        dp[0] = 1
        
        for i in range(1, m+1):
            temp = [0]*(n+1)
            temp[0] = 1
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    temp[j] = dp[j-1] + dp[j]
                else:
                    temp[j] = dp[j]
            dp = temp 

        return dp[n]