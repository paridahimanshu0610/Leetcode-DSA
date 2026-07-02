class Solution:
    def totalCoins(self, a, l, h, dp):
        if l > h:
            return 0

        if dp[l][h] is not None:
            return dp[l][h]

        maxCoins = -float('inf')
        for i in range(l, h+1):
            leftCoins = a[l-1] if l-1 >= 0 else 1
            rightCoins = a[h+1] if h+1 < len(a) else 1
            currCoins = a[i]

            totalCoins = (leftCoins*currCoins*rightCoins) + self.totalCoins(a, l, i-1, dp) + self.totalCoins(a, i+1, h, dp)
            maxCoins = max(maxCoins, totalCoins)

        dp[l][h] = maxCoins

        return maxCoins 

    def maxCoins(self, a: List[int]) -> int:
        n = len(a)
        dp = [[None] * n for _ in range(n)]

        return self.totalCoins(a, 0, n-1, dp)