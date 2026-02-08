class Solution:
    def minPathFromCurrPt(self, a, ii, jj, dp):
        if (ii==(len(a)-1)) and (jj==len(a[0])-1):
            dp[ii][jj] = a[ii][jj]
            return dp[ii][jj]

        if (ii >= len(a)) or (jj >= len(a[0])):
            return float('inf')
        
        if dp[ii][jj]!=-1:
            return dp[ii][jj]
        
        dp[ii][jj] = a[ii][jj] + min(self.minPathFromCurrPt(a, ii+1, jj, dp), self.minPathFromCurrPt(a, ii, jj+1, dp))

        return dp[ii][jj]

    def minPathSum(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        dp = [-1]*n
        dp[n-1] = a[m-1][n-1]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i==m-1) and (j==n-1):
                    continue
                right = dp[j+1] if j+1 < n else float('inf') 
                down = dp[j] if i+1 < m else float('inf')

                dp[j] = a[i][j] + min(right, down)

        return dp[0]
        