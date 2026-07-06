class Solution:
    def countSquares(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        dp = [[0]*n for _ in range(m)]
        res = 0

        for j in range(n):
            if a[0][j] == 1:
                dp[0][j] = 1
                res += 1

        for i in range(1, m):
            if a[i][0] == 1:
                dp[i][0] = 1
                res += 1

        for i in range(1, m):
            for j in range(1, n):
                if a[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    res += dp[i][j]

        return res