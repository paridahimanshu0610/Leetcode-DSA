class Solution:
    def lessThanEqualToK(self, a, k):
        res = 0
        l, r = 0, 0
        curr_set = {}

        while l <= r and r < len(a):
            curr_set[a[r]] = curr_set.get(a[r], 0) + 1

            while len(curr_set) > k:
                curr_set[a[l]] -= 1
                if curr_set[a[l]] == 0:
                    del curr_set[a[l]]
                l += 1

            if len(curr_set) <= k:
                res += (r-l+1)
            
            r += 1

        return res


    def subarraysWithKDistinct(self, a: List[int], k: int) -> int:

        return self.lessThanEqualToK(a, k)-self.lessThanEqualToK(a, k-1)