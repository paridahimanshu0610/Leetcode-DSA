class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        l, r = 0, 0
        res= 0
        cnt = 0 # Track the number of zeros

        while l <= r and r < len(a):
            if a[r]==0:
                cnt += 1
                while cnt > k:
                    if a[l]==0:
                        cnt -= 1
                    l += 1
            
            res = max(res, r-l+1)
            r += 1
        
        return res
