class Solution:
    def minSumFromCurrPt(self, a, ii, jj, dp):
        if (ii==len(a)-1) and (0<=jj<len(a[0])):
            dp[ii][jj] = a[ii][jj]
            return dp[ii][jj]

        if (ii>=len(a)) or (jj>=len(a[0])) or (jj<0):
            return float('inf')

        if dp[ii][jj]!=-1:
            return dp[ii][jj]
        
        dp[ii][jj] = a[ii][jj] + min(self.minSumFromCurrPt(a, ii+1, jj, dp), self.minSumFromCurrPt(a, ii+1, jj+1, dp), self.minSumFromCurrPt(a, ii+1, jj-1, dp))

        return dp[ii][jj]

    def minFallingPathSum(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        dp = [item for item in a[-1]]

        for ii in range(m-2, -1, -1):
            temp = []
            for jj in range(n):
                bottom = dp[jj]
                bottom_left = dp[jj-1] if jj-1 >= 0 else float('inf')
                bottom_right = dp[jj+1] if jj+1 < n else float('inf')
                temp.append(a[ii][jj] + min(bottom, bottom_left, bottom_right))
            dp = temp
            
        return min(dp) 