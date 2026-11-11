class Solution:
    def maxSubArray(self, a: list[int]) -> int:
        res = -float("inf")
        prevSum = 0

        for i in range(len(a)):
            if prevSum + a[i] > a[i]:
                prevSum = prevSum + a[i]
            else:
                prevSum = a[i]

            res = max(res, prevSum)

        return res 