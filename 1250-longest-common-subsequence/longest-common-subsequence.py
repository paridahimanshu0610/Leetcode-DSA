class Solution:
    def soFar(self, s1, s2, idx1, idx2, dp):
        if idx1 == 0:
            dp[idx1][idx2] = 1 if (s1[idx1] in s2[:idx2+1]) else 0
            return dp[idx1][idx2]
        elif idx2 == 0:
            dp[idx1][idx2] = 1 if (s2[idx2] in s1[:idx1+1]) else 0
            return dp[idx1][idx2]  
        
        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2] 

        if s1[idx1] == s2[idx2]:
            res = 1 + self.soFar(s1, s2, idx1-1, idx2-1, dp)
        else:
            res = max(self.soFar(s1, s2, idx1, idx2-1, dp), self.soFar(s1, s2, idx1-1, idx2, dp))

        dp[idx1][idx2] = res

        return dp[idx1][idx2]

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[None]*m for _ in range(n)]

        return self.soFar(s1, s2, n-1, m-1, dp)