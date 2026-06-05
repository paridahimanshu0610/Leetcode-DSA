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

    def minDistance(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [0]*n

        idx2 = 0
        while idx2 < n:
            if s1[0] == s2[idx2]:
                break
            idx2 += 1
        while idx2 < n:
            dp[idx2] = 1
            idx2 += 1

        for idx1 in range(1, m):
            temp = [0]*n
            for idx2 in range(n):
                if s1[idx1] == s2[idx2]:
                    temp[idx2] = (1 + dp[idx2-1]) if (idx2-1 >= 0) else 1
                else:
                    val = temp[idx2-1] if (idx2-1 >= 0) else 0 
                    temp[idx2] = max(val, dp[idx2])
            dp = temp

        return (n-dp[n-1]) + (m-dp[n-1])