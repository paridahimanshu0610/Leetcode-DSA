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
        dp = {}
        total = sum(a)
        lower, upper = target - total, target + total

        for k in range(lower, upper+1):
            if (k == a[0]) or (k == -a[0]):
                if k != 0:
                    dp[k] = 1
                else:
                    dp[k] = 2
            else:
                dp[k] = 0

        for idx in range(1, n):
            temp = {}
            for k in range(lower, upper+1):
                plus = dp.get(k-a[idx], 0) 
                minus = dp.get(k+a[idx], 0) 

                temp[k] = plus + minus
            dp = temp

        return dp[target]