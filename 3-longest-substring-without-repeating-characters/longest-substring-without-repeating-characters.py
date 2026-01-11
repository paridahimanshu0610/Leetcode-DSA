class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, -1
        char_idx = dict()
        candidate = (start, end)

        for i in range(len(s)):
            if s[i] in char_idx:
                start = max(char_idx[s[i]]+1, start)
        
            char_idx[s[i]] = i
            end = i
            
            # print(i, start, end, char_idx)
            if (end-start) > (candidate[1]-candidate[0]):
                candidate = (start, end)
            # print(candidate)

        return candidate[1]-candidate[0]+1