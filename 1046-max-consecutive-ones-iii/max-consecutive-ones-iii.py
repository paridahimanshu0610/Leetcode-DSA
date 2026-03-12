class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        res, zeros, l, r = 0, 0, 0, 0
        n = len(a)

        while r < n and l <= r:
            if a[r]==0:
                zeros += 1
            
            if zeros > k:
                while l < n and a[l]==1:
                    l += 1
                if l >= n:
                    break
                zeros -= 1
                l += 1
            
            curr_len = (r-l)+1
            res = max(res, curr_len)

            r += 1

        return res