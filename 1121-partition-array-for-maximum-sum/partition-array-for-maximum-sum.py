class Solution:
    def maxSum(self, a, l, k, dp):
        if l == len(a):
            return 0

        if dp[l] is not None:
            return dp[l]

        maxTotalSum = -float('inf')
        maxi = -float('inf')
        i = 0
        while i < k and l+i < len(a):
            maxi = max(maxi, a[l+i])
            maxTotalSum = max(maxTotalSum, (i+1)*maxi + self.maxSum(a, l+i+1, k, dp))
            i += 1

        dp[l] = maxTotalSum

        return dp[l] 

    def maxSumAfterPartitioning(self, a: List[int], k: int) -> int:
        n = len(a)
        dp = [None] * (n+1)
        dp[n] = 0

        for l in range(n-1, -1, -1):
            maxTotalSum = -float('inf')
            maxi = -float('inf')
            i = 0
            while i < k and l+i < n:
                maxi = max(maxi, a[l+i])
                maxTotalSum = max(maxTotalSum, (i+1)*maxi + dp[l+i+1])
                i += 1
            dp[l] = maxTotalSum 

        return dp[0]
        