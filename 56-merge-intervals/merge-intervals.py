class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort(key = lambda x:x[0])
        res = []
        curr = a[0]
        n = len(a)

        for i in range(1, n):
            temp = a[i]
            if curr[1] < temp[0]:
                res.append(curr)
                curr = temp
            else:
                curr[1] = max(curr[1], temp[1])
        
        res.append(curr)

        return res