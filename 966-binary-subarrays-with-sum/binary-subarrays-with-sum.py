class Solution:
    def getSubarray(self, a, k):
        if k < 0:
            return 0
        res = 0
        l, r = 0, 0
        curr_sum = 0

        while l<=r and r<len(a):
            curr_sum += a[r]
            if curr_sum <= k:
                res += (r-l+1)
            else:
                while l < r and curr_sum > k:
                    curr_sum -= a[l]
                    l += 1
                if curr_sum <= k:
                    res += (r-l+1)
            r += 1

        return res

    def numSubarraysWithSum(self, a: List[int], k: int) -> int:
        return self.getSubarray(a, k) - self.getSubarray(a, k-1)