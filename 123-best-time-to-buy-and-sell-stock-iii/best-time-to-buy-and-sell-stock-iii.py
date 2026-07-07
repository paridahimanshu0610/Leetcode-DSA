class Solution:
    def fromHere(self, a, idx, cap, canBuy, dp):
        if idx == len(a):
            return 0
        if cap == -1:
            return 0

        if dp[idx][cap][canBuy] is not None:
            return dp[idx][cap][canBuy]

        if canBuy==1:
            res = max(-a[idx]+self.fromHere(a, idx+1, cap, 0, dp), self.fromHere(a, idx+1, cap, 1, dp))
        else:
            res = max(a[idx]+self.fromHere(a, idx+1, cap-1, 1, dp), self.fromHere(a, idx+1, cap, 0, dp))
        
        dp[idx][cap][canBuy] = res

        return res

    def maxProfit(self, a: List[int]) -> int:
        n = len(a)
        dp = [[[None]*2 for _ in range(2)] for _ in range(n)]
        cap = 1 # For the purpose of 0-index, instead of 2, I have taken 1
        canBuy = 1

        return self.fromHere(a, 0, cap, 1, dp)