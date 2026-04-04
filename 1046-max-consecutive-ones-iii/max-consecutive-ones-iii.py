class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        l, r = 0, 0
        curr_zeros, res = 0, 0

        while l <= r and r < len(a):
            if a[r] == 0:
                curr_zeros += 1
            
            while l <= r and curr_zeros > k:
                if a[l] == 0:
                    curr_zeros -= 1
                l += 1

            if curr_zeros <= k:
                res = max(res, r-l+1)
                
            r += 1

        return res