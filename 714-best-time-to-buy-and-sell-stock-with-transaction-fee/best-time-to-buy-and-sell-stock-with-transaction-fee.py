class Solution:
    def fromThisDay(self, a, idx, toBuy, fee, dp):
        if idx >= len(a):
            return 0

        if toBuy == 1:
            totalProfit = max(-a[idx] + self.fromThisDay(a, idx+1, 0, fee, dp), self.fromThisDay(a, idx+1, 1, fee, dp))
        else:
            totalProfit = max(a[idx]-fee + self.fromThisDay(a, idx+1, 1, fee, dp), self.fromThisDay(a, idx+1, 0, fee, dp))
        
        dp[idx][toBuy] = totalProfit

        return totalProfit

    def maxProfit(self, a: List[int], fee: int) -> int:
        n = len(a)
        dp = [0]*2

        for idx in range(n-1,-1,-1):
            temp = [None]*2
            for toBuy in range(2):
                if toBuy == 1:
                    totalProfit = max(-a[idx] + dp[0], dp[1])
                else:
                    totalProfit = max(a[idx]-fee + dp[1], dp[0])
                
                temp[toBuy] = totalProfit
                
            dp = temp

        return dp[1] 