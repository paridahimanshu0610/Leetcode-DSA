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
        dp = [[None]*(target+1) for _ in range(n)]

        return self.soFar(a, n-1, target, dp)