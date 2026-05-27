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

        dp = [[None]*(target+1) for _ in range(n)]

        return self.soFar(a, n-1, target, dp)