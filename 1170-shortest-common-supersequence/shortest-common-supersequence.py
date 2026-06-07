class Solution:
    def soFar(self, s1,  s2, idx1, idx2, dp):
        if idx1 < 0 or idx2 < 0:
            return 0
        
        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2]

        if s1[idx1] == s2[idx2]:
            dp[idx1][idx2] = 1 + self.soFar(s1, s2, idx1-1, idx2-1, dp)
        else:
            dp[idx1][idx2] = max(self.soFar(s1, s2, idx1, idx2-1, dp), self.soFar(s1, s2, idx1-1, idx2, dp))

        return dp[idx1][idx2]

    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[None]*n for _ in range(m)]

        self.soFar(s1, s2, m-1, n-1, dp) 

        maxLen = m+n-dp[m-1][n-1]
        
        i, j = m-1, n-1
        res = []

        while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                res.append(s1[i])
                i -= 1
                j -= 1
            elif i == 0:
                res.append(s2[j])
                j -= 1
            elif j == 0:
                res.append(s1[i])
                i -= 1
            elif (dp[i-1][j] >= dp[i][j-1]):
                res.append(s1[i])
                i -= 1
            else:
                res.append(s2[j])
                j -= 1

        while i >= 0:
            res.append(s1[i])
            i -= 1

        while j >= 0:
            res.append(s2[j])
            j -= 1 

        return "".join(res[::-1])