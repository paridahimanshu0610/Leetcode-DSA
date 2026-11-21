class Solution:
    def maxSubarraySumCircular(self, a: list[int]) -> int:
        maxSum, minSum = float("-inf"), float("inf")
        allNeg = True
        n = len(a)
        currSum = 0

        # Finding the maximum sum subarray
        for i in range(n):
            currSum += a[i]
            currSum = max(currSum, a[i])
            maxSum = max(currSum, maxSum)
            if allNeg and (a[i] >= 0):
                allNeg = False

        if allNeg:
            return maxSum

        currSum, total = 0, 0
        # Finding the minimum sum subarray
        for i in range(n):
            total += a[i] 
            currSum += a[i]
            currSum = min(currSum, a[i])
            minSum = min(currSum, minSum)

        return max(maxSum, total-minSum)