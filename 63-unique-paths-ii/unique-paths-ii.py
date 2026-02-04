class Solution:
    def getTotalPaths(self, a, ii, jj, dp):
        if ii == len(a)-1 and jj == len(a[0])-1:
            dp[ii][jj] = 1 if a[ii][jj]==0 else 0
            return dp[ii][jj]

        if ii > len(a)-1 or jj > len(a[0])-1:
            return 0
        
        # If current cell itself is an obstacle
        if a[ii][jj] == 1:
            dp[ii][jj] = 0
            return dp[ii][jj]

        if dp[ii][jj]!=-1:
            return dp[ii][jj]

        dp[ii][jj] = self.getTotalPaths(a, ii+1, jj, dp) + self.getTotalPaths(a, ii, jj+1, dp)

        return dp[ii][jj]
             
    def uniquePathsWithObstacles(self, a: List[List[int]]) -> int:
        # dp[i][j] stores the total paths from current cell to the last cell (m-1, n-1)
        dp = [[-1]*len(a[0]) for _ in range(len(a))]
        return self.getTotalPaths(a, 0, 0, dp)