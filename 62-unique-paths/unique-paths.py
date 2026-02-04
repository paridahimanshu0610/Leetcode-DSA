class Solution:
    def getTotalPaths(self, m, n, ii, jj, dp):
        if ii == 0 or jj == 0:
            dp[ii][jj] = 1
            return 1

        if ii < 0 or jj < 0:
            return 0

        if dp[ii][jj]!=-1:
            return dp[ii][jj]

        dp[ii][jj] = self.getTotalPaths(m, n, ii-1, jj, dp) + self.getTotalPaths(m, n, ii, jj-1, dp)

        return dp[ii][jj]
             
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        return self.getTotalPaths(m, n, m-1, n-1, dp)