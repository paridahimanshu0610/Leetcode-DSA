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
        dp = [[None]*n for _ in range(m)]

        mini = float('inf')

        for i in range(n):
            mini = min(mini, self.soFar(a, m-1, i, dp))

        return mini