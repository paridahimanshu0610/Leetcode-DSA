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
                    prevLength = dp[idx2-1] if idx2-1 >= 0 else 0
                    res = 1 + prevLength
                else:
                    res = max(temp[idx2-1], dp[idx2])

                temp[idx2] = res
            dp = temp

        return dp[n-1]