class Solution:
    def maxTurbulenceSize(self, a: list[int]) -> int:
        i, j = 0, 1
        res = 1
        n = len(a)
        prev = 0

        while i <= j and j < n:
            if a[j-1] > a[j]:
                curr = -1
            elif a[j-1] < a[j]:
                curr = 1
            else:
                curr = 0

            if curr == 0:
                res = max(j-i, res)
                i = j
            elif prev*curr != -1:
                res = max(j-i, res)
                i = j-1
            
            prev = curr
            j += 1

        return max(j-i, res)