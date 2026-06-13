class Solution:
    def soFar(self, s, p, idx1, idx2, dp):
        if idx1 < 0:
            if idx2 < 0:
                return True
            else:
                for i in range(idx2+1):
                    if p[i] != "*":
                        return False
                return True
        elif idx2 < 0:
            return idx1 < 0
        
        if dp[idx1][idx2] is not None:
            return dp[idx1][idx2]

        if s[idx1] == p[idx2]:
            dp[idx1][idx2] = self.soFar(s, p, idx1-1, idx2-1, dp)
        else:
            if p[idx2] == "*":
                dp[idx1][idx2] = self.soFar(s, p, idx1-1, idx2-1, dp) or self.soFar(s, p, idx1, idx2-1, dp) or self.soFar(s, p, idx1-1, idx2, dp)
            elif p[idx2] == "?":
                dp[idx1][idx2] = self.soFar(s, p, idx1-1, idx2-1, dp)
            else:
                dp[idx1][idx2] = False

        return dp[idx1][idx2]

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp = [[None]*n for _ in range(m)]
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1, n+1):
            if p[i-1] == "*":
                dp[i] = True
            else:
                break

        for idx1 in range(1, m+1):
            temp = [False]*(n+1)
            for idx2 in range(1, n+1):
                if s[idx1-1] == p[idx2-1]:
                    temp[idx2] = dp[idx2-1]
                else:
                    if p[idx2-1] == "*":
                        temp[idx2] = dp[idx2-1] or dp[idx2] or temp[idx2-1]
                    elif p[idx2-1] == "?":
                        temp[idx2] = dp[idx2-1]
                    else:
                        temp[idx2] = False

            dp = temp

        return dp[n]