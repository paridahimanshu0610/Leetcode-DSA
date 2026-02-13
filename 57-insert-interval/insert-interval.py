class Solution:
    def insert(self, a: List[List[int]], new_i: List[int]) -> List[List[int]]:
        res = []
        n = len(a)
        i = 0

        while i < n and a[i][1] < new_i[0]:
            res.append(a[i])
            i += 1
        
        while i < n and a[i][0] <= new_i[1]:
            new_i[0] = min(a[i][0], new_i[0])
            new_i[1] = max(a[i][1], new_i[1])
            i += 1

        res.append(new_i)

        while i < n:
            res.append(a[i])
            i += 1

        return res