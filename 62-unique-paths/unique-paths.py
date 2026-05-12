class Solution:
    def walk(self, m, n, i, j, dp):
        if i == 0 or j== 0:
            dp[i][j] = 1
            return 1
        
        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = self.walk(m, n, i-1, j, dp) + self.walk(m, n, i, j-1, dp)
        
        return dp[i][j] 

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]

        return self.walk(m, n, m-1, n-1, dp)