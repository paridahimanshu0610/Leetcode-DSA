class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        curr_dict = {}
        target = {'a', 'b', 'c'}

        while l <= r and r < len(s):
            if s[r] in target:
                curr_dict[s[r]] = curr_dict.get(s[r], 0) + 1

            while len(curr_dict)>=3 and l <= r:
                res += (len(s) - r)
                if s[l] in target:
                    curr_dict[s[l]] -= 1
                    if curr_dict[s[l]] == 0:
                        del curr_dict[s[l]]
                l += 1

            r += 1

        return res  
