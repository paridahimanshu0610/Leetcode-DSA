class Solution:
    def get_min_path_sum(self, a, ii, jj, dp):
        if ii==len(a)-1 and jj==len(a[0])-1:
            dp[ii][jj] = a[ii][jj]
            return a[ii][jj]

        if ii > len(a)-1 or jj > len(a[0])-1:
            return float('inf')
        
        if dp[ii][jj]!=-1:
            return dp[ii][jj]
        
        dp[ii][jj] = a[ii][jj] + min(self.get_min_path_sum(a, ii+1, jj, dp), self.get_min_path_sum(a, ii, jj+1, dp))

        return dp[ii][jj]

    def minPathSum(self, a: List[List[int]]) -> int:
        dp = [[-1]*len(a[0]) for _ in range(len(a))]
        m, n = len(a), len(a[0])
        dp[m-1][n-1] = a[m-1][n-1]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i==m-1 and j==n-1:
                    continue
                right = dp[i][j+1] if j+1 < n else float('inf')
                down = dp[i+1][j] if i+1 < m else float('inf')
                dp[i][j] = a[i][j] + min(right, down)

        return dp[0][0]