class Solution:
    def nextSmallerEle(self, a):
        n = len(a)
        res = [None] * n
        stack = []

        for i in range(n):
            if (len(stack) == 0) or (a[i] >= a[stack[-1]]):
                stack.append(i)
            else:
                while len(stack) > 0 and a[stack[-1]] > a[i]:
                    res[stack[-1]] = i  # a[i]
                    stack.pop()
                stack.append(i)

        while len(stack) > 0:
            res[stack[-1]] = n
            stack.pop()

        return res

    def prevSmallerEle(self, a):
        n = len(a)
        res = [None] * n
        stack = []

        for i in range(n - 1, -1, -1):
            if len(stack) == 0 or a[i] >= a[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and a[stack[-1]] > a[i]:
                    res[stack[-1]] = i  # a[i]
                    stack.pop()
                stack.append(i)

        while len(stack) > 0:
            res[stack[-1]] = -1
            stack.pop()

        return res

    def largestRectangleArea(self, a: List[int]) -> int:
        pse, nse = self.prevSmallerEle(a), self.nextSmallerEle(a)

        n = len(a)
        res = -float("inf")

        for i in range(n):
            res = max(res, (nse[i] - pse[i] - 1) * a[i])

        return res

    def maximalRectangle(self, a: List[List[str]]) -> int:
        m, n = len(a), len(a[0])
        hist = [0]*n
        res = -float('inf')

        for i in range(m):
            hist = [(hist[j] + 1) if (a[i][j]=="1") else 0 for j in range(n)]   
            res = max(res, self.largestRectangleArea(hist))

        return res