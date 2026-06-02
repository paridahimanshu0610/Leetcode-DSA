class Solution:
    def soFar(self, a, idx, k, dp):
        if k == 0:
            dp[idx][k] = 1
            return dp[idx][k]
        
        if idx == 0:
            if k % a[idx] == 0:
                dp[idx][k] = 1
            else:
                dp[idx][k] = 0
            return dp[idx][k]

        if dp[idx][k] is not None:
            return dp[idx][k]

        notTake = self.soFar(a, idx-1, k, dp)
        take = 0
        if a[idx] <= k:
            take = self.soFar(a, idx, k-a[idx], dp)
        
        dp[idx][k] = take + notTake

        return dp[idx][k]

    def change(self, target: int, a: List[int]) -> int:
        n = len(a)
        dp = [0]*(target+1)
        dp[0] = 1
        
        if a[0] <= target:
            for k in range(target+1):
                if k % a[0] == 0:
                    dp[k] = 1 

        for idx in range(1, n):
            temp = [0]*(target+1)
            temp[0] = 1
            for k in range(target+1):          
                notTake = dp[k]
                take = 0
                if a[idx] <= k:
                    take = temp[k-a[idx]]
                temp[k] = take + notTake

            dp = temp

        return dp[target]