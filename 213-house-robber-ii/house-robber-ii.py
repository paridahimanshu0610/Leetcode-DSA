class Solution:
    def rob(self, a: List[int]) -> int:
        if len(a) == 1:
            return a[0]
        elif len(a) == 2:
            return max(a)

        prev1, prev2 = a[0], 0
        for i in range(1, len(a)-1):
            prev1, prev2 = max(a[i]+prev2, prev1), prev1
        res = max(prev1, prev2)

        prev1, prev2 = a[1], 0
        for i in range(2, len(a)):
            prev1, prev2 = max(a[i]+prev2, prev1), prev1
        res = max(prev1, prev2, res)

        return res