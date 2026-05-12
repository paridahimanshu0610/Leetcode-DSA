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
        dp = [0]*n

        for i in range(n):
            if a[0][i] == 1:
                break
            dp[i] = 1
        
        for i in range(1, m):
            for j in range(n):
                if a[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] = dp[j] + dp[j-1] if j-1 >= 0 else dp[j]
        
        return dp[-1]