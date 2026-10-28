class Solution:
    def canJump(self, a: list[int]) -> bool:
        n = len(a)
        j = min(a[0], n-1) # Current maximum reachable index

        for i in range(1, n):
            if i <= j:
                j = max(j, min(i+a[i], n-1))
            else:
                return False

        return True