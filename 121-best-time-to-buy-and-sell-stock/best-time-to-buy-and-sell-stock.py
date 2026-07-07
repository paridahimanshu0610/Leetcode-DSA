class Solution:
    def maxProfit(self, a: List[int]) -> int:
        n, curr, res = len(a), a[0], 0

        for i in range(1, n):
            if a[i] <= curr:
                curr = a[i]
            else:
                res = max(res, a[i]-curr)

        return res