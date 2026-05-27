class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        n = len(a)
        res = [None]*n
        i, j = 0, 1

        for e in a:
            if e >= 0:
                res[i] = e
                i += 2
            else:
                res[j] = e
                j += 2

        return res