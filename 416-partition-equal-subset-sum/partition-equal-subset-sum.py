class Solution:
    def canPartition(self, a: List[int]) -> bool:
        total = sum(a)
        if total % 2 == 1:
            return False
        target0 = total // 2

        dp = [False]*(target0+1)
        dp[0] = True

        n = len(a)
        for idx in range(1, n+1):
            temp = [False]*(target0+1)
            temp[0] = True
            for target in range(1, target0+1):
                notTake = dp[target]
                take = False
                if a[idx-1] <= target:
                    take = dp[target-a[idx-1]]
                temp[target] = (take or notTake)
            dp = temp

        return dp[target0]