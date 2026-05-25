class Solution:
    def soFar(self, a, r, c, dp):
        if r < 0 or c < 0 or c >= len(a[0]):
            return float('inf') 
        
        if r == 0:
            dp[r][c] = a[r][c]
            return dp[r][c]

        if dp[r][c] is not None:
            return dp[r][c]

        mini = float('inf')
        for j in range(c-1, c+2):
            mini = min(mini, self.soFar(a, r-1, j, dp))

        mini = a[r][c] + mini
        dp[r][c] = mini

        return mini
        

    def minFallingPathSum(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        dp = [a[0][i] for i in range(n)]

        for i in range(1, m):
            temp = [None]*n
            for j in range(n):
                topLeft = dp[j-1] if j-1 >= 0 else float('inf')
                topRight = dp[j+1] if j+1 < n else float('inf')
                top = dp[j]
                temp[j] = a[i][j] + min(topLeft, top, topRight)
            dp = temp

        return min(dp)