class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        n = len(a)
        extremePts = [[None, None] for _ in range(n)]

        stack = []
        for i in range(n):
            while len(stack) > 0 and stack[-1][0] >= a[i]:
                _, idx = stack.pop()
                extremePts[idx][1] = i-1
            stack.append([a[i], i])

        while len(stack)!=0:
            _, idx = stack.pop()
            extremePts[idx][1] = n-1

        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and stack[-1][0] > a[i]:
                _, idx = stack.pop()
                extremePts[idx][0] = i+1
            stack.append([a[i], i])

        while len(stack)!=0:
            _, idx = stack.pop()
            extremePts[idx][0] = 0
        
        res = 0

        for i in range(n):
            n1, n2 = (extremePts[i][1]-i), (i-extremePts[i][0])
            res += ((n1+n2+n1*n2+1)*a[i])%(10**9 + 7)

        return res%(10**9 + 7)