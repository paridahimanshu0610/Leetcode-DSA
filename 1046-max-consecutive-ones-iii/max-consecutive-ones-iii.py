class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        res, zeros, l, r = 0, 0, 0, 0
        n = len(a)

        while r < n and l <= r:
            if a[r] == 0:
                zeros += 1

            if zeros > k:
                if a[l] == 0:
                    zeros -= 1
                l += 1
            
            if zeros <= k:
                res = max(res, r-l+1)
            
            r += 1   

        return res