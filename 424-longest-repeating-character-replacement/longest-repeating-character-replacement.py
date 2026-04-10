class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l, r = 0, 0
        res = 0

        while l <= r and r < len(s):
            freq[s[r]] = freq.get(s[r], 0)+1

            max_freq = max(freq.values())
            curr_window_len = r-l+1

            if (curr_window_len - max_freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
                curr_window_len = r-l+1
                max_freq = max(freq.values())

            if (curr_window_len - max_freq) <= k:
                res = max(res, curr_window_len)

            r += 1

        return res 