class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res= 0
        freq = {}

        while l <= r and r < len(s):
            if s[r] in freq and freq[s[r]] >= l:
                l = freq[s[r]] + 1
            freq[s[r]] = r

            res = max(res, r-l+1)
            r += 1

        return res