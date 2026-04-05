class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        curr_set = set()
        res = 0

        while l <= r and r < len(s):
            if s[r] not in curr_set:
                curr_set.add(s[r])
                res = max(res, r-l+1)
            else:
                while s[l] != s[r]:
                    curr_set.remove(s[l])
                    l += 1
                l += 1
            
            r += 1

        return res