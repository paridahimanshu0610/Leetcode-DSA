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
        dp = [0]*n

        for idx1 in range(1, n):
            temp = [0]*n
            for idx2 in range(n-1, -1, -1):
                if idx2 >= idx1:
                    temp[idx2] = 0
                elif s[idx1] == s[idx2]:
                    temp[idx2] = dp[idx2+1]
                else:
                    temp[idx2] = 1 + min(temp[idx2+1], dp[idx2])
            dp = temp

        return dp[0]