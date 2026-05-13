class Solution:
    def match(self, s1, s2, i, j, dp):
        if i < 0 or j < 0:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = 1 + self.match(s1, s2, i-1, j-1, dp) 
        else:
            dp[i][j] = max(self.match(s1, s2, i, j-1, dp), self.match(s1, s2, i-1, j, dp))

        return dp[i][j]

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        dp = [[-1]*len(s2) for _ in range(len(s1))]

        return self.match(s1, s2, len(s1)-1, len(s2)-1, dp)   