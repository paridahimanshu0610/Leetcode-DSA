class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        currMax, globalMax = -float('inf'), -float('inf')

        for i in range(len(a)):
            currMax = max(currMax + a[i], a[i])
            globalMax = max(currMax, globalMax)

        return globalMax