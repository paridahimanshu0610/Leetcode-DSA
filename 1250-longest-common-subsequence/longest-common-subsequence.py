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
        dp = [[0]*m for _ in range(n)]

        idx2 = 0
        while idx2 < m:
            if s1[0] == s2[idx2]:
                break
            idx2 += 1

        while idx2 < m:
            dp[0][idx2] = 1
            idx2 += 1

        idx1 = 0
        while idx1 < n:
            if s2[0] == s1[idx1]:
                break
            idx1 += 1

        while idx1 < n:
            dp[idx1][0] = 1
            idx1 += 1

        for idx1 in range(1, n):
            for idx2 in range(1, m):
                if s1[idx1] == s2[idx2]:
                    res = 1 + dp[idx1-1][idx2-1]
                else:
                    res = max(dp[idx1][idx2-1], dp[idx1-1][idx2])

                dp[idx1][idx2] = res

        return dp[n-1][m-1]