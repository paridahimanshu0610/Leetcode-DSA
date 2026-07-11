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
        dp = [[0]*2 for _ in range(maxCooldownWait+1)]

        for idx in range(n-1, -1, -1):
            temp = [[None]*2 for _ in range(maxCooldownWait+1)]

            for cooldownWait in range(maxCooldownWait+1):
                for toBuy in range(2):
                    if toBuy == 1:
                        if cooldownWait == 0:
                            totalProfit = max(-a[idx] + dp[0][0], dp[0][1])
                        else:
                            totalProfit = dp[cooldownWait-1][1]
                    else:
                        totalProfit = max(a[idx] + dp[maxCooldownWait][1], dp[cooldownWait][0])

                    temp[cooldownWait][toBuy] = totalProfit

            dp = temp

        return dp[0][1]