class Solution:
    def minTotalFromCurrPt(self, a, ii, jj, dp):
        if (ii==len(a)-1) and (0<=jj<len(a[-1])):
            dp[ii][jj] = a[ii][jj]
            return dp[ii][jj]
        
        if (ii>=len(a)) or (jj>=len(a[ii])):
            return float('inf')
        
        if dp[ii][jj]!=-1:
            return dp[ii][jj]
        
        dp[ii][jj] = a[ii][jj] + min(self.minTotalFromCurrPt(a, ii+1, jj, dp), self.minTotalFromCurrPt(a, ii+1, jj+1, dp))

        return dp[ii][jj]
    
    def minimumTotal(self, a: List[List[int]]) -> int:
        dp = []
        dp = [item for item in a[-1]]
        
        for i in range(len(a)-2, -1, -1):
            for j in range(len(a[i])):
                dp[j] = a[i][j] + min(dp[j], dp[j+1])
        
        return dp[0]