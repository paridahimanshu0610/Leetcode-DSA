class Solution:
    def fromThisDay(self, a, idx, toBuy, cooldownWait, maxCooldownWait, dp):
        if idx >= len(a):
            return 0

        if dp[idx][cooldownWait][toBuy] is not None:
            return dp[idx][cooldownWait][toBuy] 

        if toBuy == 1:
            if cooldownWait == 0:
                totalProfit = max(-a[idx] + self.fromThisDay(a, idx+1, 0, 0, maxCooldownWait, dp), self.fromThisDay(a, idx+1, 1, 0, maxCooldownWait, dp))
            else:
                totalProfit = self.fromThisDay(a, idx+1, 1, cooldownWait-1, maxCooldownWait, dp)
        else:
            totalProfit = max(a[idx] + self.fromThisDay(a, idx+1, 1, maxCooldownWait, maxCooldownWait, dp), self.fromThisDay(a, idx+1, 0, cooldownWait, maxCooldownWait, dp))
        

        dp[idx][cooldownWait][toBuy] = totalProfit 

        return totalProfit 

    def maxProfit(self, a: List[int]) -> int:
        n = len(a)
        maxCooldownWait = 1
        dp = [[[None]*2 for _ in range(maxCooldownWait+1)] for _ in range(n)]

        idx, toBuy, cooldownWait = 0, 1, 0

        return self.fromThisDay(a, idx, toBuy, cooldownWait, maxCooldownWait, dp)