class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res= 0
        freq = {}

        while l <= r and r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l += 1

            res = max(res, r-l+1)
            r += 1

        return res