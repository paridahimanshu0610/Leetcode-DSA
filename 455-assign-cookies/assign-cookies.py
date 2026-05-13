class Solution:
    def findContentChildren(self, c: List[int], b: List[int]) -> int:
        b.sort()
        c.sort()
        
        res = 0
        j = 0

        for i in range(len(c)):
            while j < len(b):
                if b[j] >= c[i]:
                    res += 1
                    j += 1
                    break
                j += 1

        return res