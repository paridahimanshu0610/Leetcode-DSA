class Solution:
    def canJump(self, a: list[int]) -> bool:
        maxReachIdx = 0
        n = len(a)

        for i in range(n):
            if i <= maxReachIdx:
                maxReachIdx = max(maxReachIdx, i+a[i])
            else:
                return False

            # Early stopping
            if maxReachIdx >= len(a)-1:
                return True

        return True