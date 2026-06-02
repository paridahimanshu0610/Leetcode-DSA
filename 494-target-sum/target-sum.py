class Solution:
    def soFar(self, a, idx, k, dp):
        if idx == 0:
            if (k == a[idx]) or (k == -a[idx]):
                if k != 0:
                    dp[(idx, k)] = 1
                else:
                    dp[(idx, k)] = 2
            else:
                dp[(idx, k)] = 0

            return dp[(idx, k)]
        
        if (idx, k) in dp:
            return dp[(idx, k)]
        
        plus = self.soFar(a, idx-1, k-a[idx], dp)
        minus = self.soFar(a, idx-1, k+a[idx], dp)

        dp[(idx, k)] = plus + minus

        return dp[(idx, k)]

    def findTargetSumWays(self, a: List[int], target: int) -> int:
        n = len(a)
        total = sum(a)
        lower, upper = target - total, target + total
        dp = [0]*(2*total+1)

        for k in range(lower, upper+1):
            if (k == a[0]) or (k == -a[0]):
                if k != 0:
                    dp[k-lower] = 1
                else:
                    dp[k-lower] = 2
            else:
                dp[k-lower] = 0

        for idx in range(1, n):
            temp = [0]*(2*total+1)
            for k in range(lower, upper+1):
                plus, minus = 0, 0
                if 0 <= k-a[idx]-lower <= 2*total:
                    plus = dp[k-a[idx]-lower]
                if 0 <= k+a[idx]-lower <= 2*total:  
                    minus = dp[k+a[idx]-lower]
                temp[k-lower] = plus + minus

            dp = temp

        return dp[target-lower]