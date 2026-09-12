class Solution:
    def maxRectangleHistogram(self, a: List[int]) -> int:
        n = len(a)
        wrange = [[None, None] for _ in range(n)]

        stack = []  
        for i in range(n):
            while len(stack) > 0 and a[i] < stack[-1][0]:
                _, idx = stack.pop()
                wrange[idx][1] = i-1
            stack.append([a[i], i])

        while len(stack) > 0:
            _, idx = stack.pop()
            wrange[idx][1] = n-1    

        stack = []  
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and a[i] < stack[-1][0]:
                _, idx = stack.pop()
                wrange[idx][0] = i+1
            stack.append([a[i], i])

        while len(stack) > 0:
            _, idx = stack.pop()
            wrange[idx][0] = 0

        res = -1
        for i in range(n):
            res = max(res, (wrange[i][1] - wrange[i][0] + 1)*a[i])

        return res

    def maximalRectangle(self, a: List[List[str]]) -> int:
        m, n = len(a), len(a[0])

        hist = [0]*n
        res = -1

        for i in range(m):
            for j in range(n):
                hist[j] = (hist[j]+1) if a[i][j]=="1" else 0
            res = max(res, self.maxRectangleHistogram(hist))

        return res