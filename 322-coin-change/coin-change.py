class Solution:
    def soFar(self, a, idx, k, dp):
        if k == 0:
            dp[idx][k] = 0
            return dp[idx][k]
        
        if idx == 0:
            if k % a[idx] == 0:
                dp[idx][k] = k // a[idx]
            else:
                dp[idx][k] = -1
            return dp[idx][k]
        
        if dp[idx][k] is not None:
            return dp[idx][k]

        notTake = self.soFar(a, idx-1, k, dp)

        take = -1
        if a[idx] <= k:
            temp = self.soFar(a, idx, k-a[idx], dp)
            if temp >= 0: 
                take = 1 + temp
        
        if take >=0 and notTake >= 0:
            dp[idx][k] = min(take, notTake)
        elif take >= 0:
            dp[idx][k] = take
        elif notTake >= 0:
            dp[idx][k] = notTake
        else:
            dp[idx][k] = -1

        return dp[idx][k]

    def coinChange(self, a: List[int], target: int) -> int:
        n = len(a)
        dp = [-1]*(target+1)
        dp[0] = 0

        if a[0] <= target:
            for k in range(1, target+1):
                if k % a[0] == 0:
                    dp[k] = k // a[0]

        for idx in range(1, n):
            temp = [-1]*(target+1)
            temp[0] = 0
            for k in range(1, target+1):
                notTake = dp[k]

                take = -1
                if a[idx] <= k:
                    temp0 = temp[k-a[idx]]
                    if temp0 >= 0: 
                        take = 1 + temp0
                
                if take >=0 and notTake >= 0:
                    temp[k] = min(take, notTake)
                elif take >= 0:
                    temp[k] = take
                elif notTake >= 0:
                    temp[k] = notTake
                else:
                    temp[k] = -1
            dp = temp

        return dp[target] 