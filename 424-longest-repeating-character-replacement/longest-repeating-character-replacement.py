class Solution:
    def get_highest_frequency(self, freq):
        return sorted(freq.items(), key=lambda x:x[1], reverse=True)[0]

    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        freq = {}
        max_freq = 0

        while l <= r and r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            item, f = self.get_highest_frequency(freq)
            n = (r-l+1)
            if (n-f) <= k:
                res = max(res, n)
            else:
                freq[s[l]] -= 1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l += 1
            r += 1

        return res 