class Solution:
    def fromThisDay(self, a, idx, toBuy, fee, dp):
        if idx >= len(a):
            return 0

        if dp[idx][toBuy] is not None:
            return dp[idx][toBuy]
             
        if toBuy == 1:
            totalProfit = max(-a[idx] + self.fromThisDay(a, idx+1, 0, fee, dp), self.fromThisDay(a, idx+1, 1, fee, dp))
        else:
            totalProfit = max(a[idx]-fee + self.fromThisDay(a, idx+1, 1, fee, dp), self.fromThisDay(a, idx+1, 0, fee, dp))
        
        dp[idx][toBuy] = totalProfit

        return totalProfit

    def maxProfit(self, a: List[int], fee: int) -> int:
        n = len(a)
        idx, toBuy = 0, 1

        dp = [[None]*2 for _ in range(n)]

        return self.fromThisDay(a, idx, toBuy, fee, dp)