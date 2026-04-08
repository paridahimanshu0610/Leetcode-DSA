class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        curr_idx = {}

        while l <= r and r < len(s):
            curr_idx[s[r]] = r

            if len(curr_idx)==3:
                res += (min(curr_idx.values()) + 1)
            
            r += 1
        
        return res