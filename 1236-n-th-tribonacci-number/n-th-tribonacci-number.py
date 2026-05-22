class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        prev1, prev2, prev3 = 1, 1, 0

        for i in range(3, n+1):
            prev1, prev2, prev3 = (prev1+prev2+prev3), prev1, prev2

        return prev1