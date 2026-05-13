class Solution:
    def total(self, a, idx, target, dp):
        if target == 0:
            return 0

        if idx == 0:
            if target % a[idx] == 0:
                return target // a[idx]
            else:
                return float('inf')

        if dp[idx][target] != -1:
            return dp[idx][target]

        # Take the coin
        take = float('inf')
        if target >= a[idx]:
            take = 1 + self.total(a, idx, target - a[idx], dp)

        # Do not take the coin
        not_take = self.total(a, idx - 1, target, dp)

        dp[idx][target] = min(take, not_take)

        return dp[idx][target]

    def coinChange(self, a: List[int], target: int) -> int:
        n = len(a)

        dp = [[-1] * (target + 1) for _ in range(n)]

        res = self.total(a, n - 1, target, dp)

        return -1 if res == float('inf') else res