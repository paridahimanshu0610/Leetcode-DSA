class Solution:
    def minPathSum(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])

        dp = [0]*n
        dp[0] = a[0][0]

        for i in range(1, n):
            dp[i] = a[0][i] + dp[i-1]

        for i in range(1, m):
            for j in range(n):
                dp[j] = a[i][j] + dp[j] if j == 0 else a[i][j] + min(dp[j-1], dp[j])

        return dp[-1]