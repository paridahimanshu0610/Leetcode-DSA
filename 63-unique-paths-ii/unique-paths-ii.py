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
        dp = [[-1]*n for _ in range(m)]
        return self.total_paths(a, 0, 0, dp)