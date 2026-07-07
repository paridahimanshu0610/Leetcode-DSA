class Solution:
    def maxProfit(self, a: List[int]) -> int:
        curr, res = a[0], 0

        for i in range(1, len(a)):
            if a[i] >= curr:
                res += (a[i]-curr)

            curr = a[i]

        return res