class Solution:
    def arrayRankTransform(self, b: list[int]) -> list[int]:
        if len(b) == 0:
            return []

        a = b.copy()
        a.sort()
        temp = {}
        
        curr_e, curr_rank = a[0], 1
        temp[curr_e] = curr_rank

        for i in range(1, len(a)):
            if a[i] != curr_e:
                curr_e, curr_rank = a[i], curr_rank+1
                temp[curr_e] = curr_rank

        return [temp[e] for e in b]