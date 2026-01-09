class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0

        cookie_idx = 0
        child_idx = 0

        while child_idx < len(g) and cookie_idx < len(s):
            if s[cookie_idx] >= g[child_idx]:
                child_idx += 1

            cookie_idx += 1

        return child_idx