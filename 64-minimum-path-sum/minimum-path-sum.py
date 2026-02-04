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
        return self.get_min_path_sum(a, 0, 0, dp)