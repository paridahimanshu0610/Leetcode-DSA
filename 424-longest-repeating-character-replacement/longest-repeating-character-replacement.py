class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # res = 0

        # for i in range(len(s)):
        #     freq = dict()
        #     freq[s[i]] = freq.get(s[i], 0)+1
        #     max_freq = 1
        #     for j in range(i+1, len(s)):
        #         freq[s[j]] = freq.get(s[j], 0)+1
        #         max_freq = max(max_freq, freq[s[j]])
        #         if k >= (j-i+1)-max_freq:
        #             res = max(res, j-i+1)
        #         else:
        #             break

        res = 0
        freq = {}
        max_freq = 0
        i = 0

        j = 0
        while j < len(s):
            freq[s[j]] = freq.get(s[j], 0)+1
            max_freq = max(max_freq, freq[s[j]])
            if (j-i+1)-max_freq <= k:
                res = max(res, j-i+1)
            else:
                while (i < j) and ((j-i+1)-max_freq) > k:
                    freq[s[i]] -= 1
                    i += 1
                    max_freq = max(freq.values())
                res = max(res, j-i+1)
            
            j+=1

        return res