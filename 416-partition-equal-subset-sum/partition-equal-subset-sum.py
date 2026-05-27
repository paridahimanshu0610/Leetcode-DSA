class Solution:
    def soFar(self, a, idx, t1, dp):
        if idx == 0:
            dp[idx][t1] = (t1 == a[0])
            return dp[idx][t1]
        
        if dp[idx][t1] is not None:
            return dp[idx][t1]

        take = False
        # Take condition
        if a[idx] <= t1:
            take = self.soFar(a, idx-1, t1-a[idx], dp)
        
        notTake = self.soFar(a, idx-1, t1, dp)

        dp[idx][t1] = (take or notTake)

        return dp[idx][t1] 

    def canPartition(self, a: List[int]) -> bool:
        target = sum(a)
        if target % 2 == 1:
            return False

        target = target // 2
        n = len(a)

        dp = [False]*(target+1)

        if a[0] <= target:
            dp[a[0]] = True

        for idx in range(1, n):
            temp = [None]*(target+1)
            for t1 in range(target+1):
                take = False
                # Take condition
                if a[idx] <= t1:
                    take = dp[t1-a[idx]]
                
                notTake = dp[t1]

                temp[t1] = (take or notTake)

            dp = temp

        return dp[target]