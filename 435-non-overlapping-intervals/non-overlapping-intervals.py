class Solution:
    def eraseOverlapIntervals(self, a: List[List[int]]) -> int:
        a.sort(key = lambda x: (x[0], x[1]))
        print(a)
        curr = a[0]
        n = len(a)
        res = 0

        for i in range(1, n):
            temp = a[i]

            if curr[1] > temp[0]:
                res += 1
                curr = curr if curr[1] < temp[1] else temp
            else:
                curr = temp
        
        return res