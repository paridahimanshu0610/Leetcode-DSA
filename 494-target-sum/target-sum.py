class Solution:
    def soFar(self, a, idx, k, dp):
        if idx == 0:
            if k == 0:
                return 2 if a[idx] == 0 else 0
            else:
                return 1 if (a[idx] == k) or (a[idx] == -k) else 0

        if (idx,k) in dp:
            return dp[(idx,k)]

        add = self.soFar(a, idx-1, k - a[idx], dp)
        subtract = self.soFar(a, idx-1, k + a[idx], dp)

        dp[(idx,k)] = add + subtract

        return dp[(idx,k)]

    def findTargetSumWays(self, a: List[int], target: int) -> int:
        n = len(a)
        dp = {}

        return self.soFar(a, n-1, target, dp)