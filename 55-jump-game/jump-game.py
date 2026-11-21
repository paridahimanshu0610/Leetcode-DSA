class Solution:
    def canJump(self, a: list[int]) -> bool:
        maxReachIdx = 0
        n = len(a)

        for i in range(n-1):
            if i <= maxReachIdx:
                maxReachIdx = max(maxReachIdx, i+a[i])
            else:
                break

            # Early stopping
            if maxReachIdx >= len(a)-1:
                return True

        return maxReachIdx >= n-1  