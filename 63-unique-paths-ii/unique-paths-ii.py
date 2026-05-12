class Solution:
    def walk(self, a, i, j, dp):
        if i < 0 or j < 0:
            return 0
        
        if a[i][j] == 1:
            dp[i][j] = 0
            return dp[i][j]

        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = self.walk(a, i-1, j, dp) + self.walk(a, i, j-1, dp)

        return dp[i][j]

    def uniquePathsWithObstacles(self, a: List[List[int]]) -> int:
        if a[0][0] == 1:
            return 0
        m, n = len(a), len(a[0])

        dp = [[-1]*n for _ in range(m)]
        dp[0][0] = 1

        return self.walk(a, m-1, n-1, dp)