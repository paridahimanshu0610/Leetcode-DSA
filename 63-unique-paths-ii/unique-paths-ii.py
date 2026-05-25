class Solution:
    def soFar(self, a, r, c, dp):
        if r == 0 and c == 0:
            if a[r][c] == 0:
                dp[r][c] = 1
            else:
                dp[r][c] = 0

            return dp[r][c]
        
        if r < 0 or c < 0:
            return 0

        if dp[r][c] != None:
            return dp[r][c]

        if a[r][c] == 1:
            dp[r][c] = 0
            return dp[r][c] 

        dp[r][c] = self.soFar(a, r-1, c, dp) + self.soFar(a, r, c-1, dp)

        return dp[r][c] 

    def uniquePathsWithObstacles(self, a: List[List[int]]) -> int:
        m , n = len(a), len(a[0])
        dp = [0]*n

        for j in range(n):
            if a[0][j] == 0:
                dp[j] = 1
            else:
                break
        
        for i in range(1, m):
            for j in range(n):
                if a[i][j] == 0:
                    dp[j] = dp[j] + (dp[j-1] if j-1 >= 0 else 0)
                else:
                    dp[j] = 0

        return dp[n-1]