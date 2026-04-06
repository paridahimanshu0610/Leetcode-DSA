class Solution:
    def longestNiceSubarray(self, a: List[int]) -> int:
        l, r = 0, 0
        curr, res = 0, 0

        while l <= r and r < len(a):
            while l <= r and curr & a[r]:
                curr ^= a[l]
                l += 1
            res = max(res, r-l+1)
            curr |= a[r]
            r += 1

        return res
