class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0

        cookie_idx = 0
        child_idx = 0

        while child_idx < len(g) and cookie_idx < len(s):
            while cookie_idx < len(s) and s[cookie_idx] < g[child_idx]:
                cookie_idx += 1
            
            if cookie_idx < len(s):
                res += 1
                cookie_idx += 1
                child_idx+=1

        return res