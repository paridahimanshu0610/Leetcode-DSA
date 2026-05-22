class Solution:
    def climbStairs(self, n: int) -> int:
        p1, p2 = 1, 0

        i = 1

        while i <= n:
            temp = p1 + p2
            p1, p2 = temp, p1
            i += 1

        return p1   