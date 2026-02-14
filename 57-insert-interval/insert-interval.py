class Solution:
    def insert(self, a: List[List[int]], new_i: List[int]) -> List[List[int]]:
        i, n = 0, len(a)

        while i < n and a[i][1] < new_i[0]:
            i += 1

        if i == n:
            return a + [new_i]
        elif i == 0 and new_i[1] < a[i][0]:
            return [new_i] + a
        elif new_i[1] < a[i][0]:
            return a[0:i] + [new_i] + a[i:] 
        
        res = a[0:i]
        curr = [min(a[i][0], new_i[0]), max(a[i][1], new_i[1])]

        for j in range(i, n):
            temp = a[j]
            if curr[1] < temp[0]:
                res.append(curr)
                curr = temp
            else:
                curr = [min(curr[0], temp[0]), max(curr[1], temp[1])]

        res.append(curr)

        return res