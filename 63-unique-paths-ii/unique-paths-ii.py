class Solution:
    def total_paths(self, a, x, y, dp):
        if (x >= len(a)) or (y>=len(a[0])) or (a[x][y]==1):
            return 0
        
        if (x==len(a)-1) and (y==len(a[0])-1):
            return 1
        
        if dp[x][y]!=-1:
            return dp[x][y]

        dp[x][y] = self.total_paths(a, x+1, y, dp) + self.total_paths(a, x, y+1, dp)
        return dp[x][y]

    def uniquePathsWithObstacles(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        if a[m-1][n-1]==1:
            return 0
        
        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        
        for j in range(n-2, -1, -1):
            if a[m-1][j]==1:
                break
            dp[m-1][j] = 1

        for i in range(m-2, -1, -1):
            if a[i][n-1]==1:
                break
            dp[i][n-1] = 1

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if a[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j] = dp[i+1][j]+dp[i][j+1]

        return dp[0][0]