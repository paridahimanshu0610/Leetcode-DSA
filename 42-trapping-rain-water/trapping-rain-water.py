class Solution:
    def trap(self, a: List[int]) -> int:
        n = len(a)
        rightBdr = [None]*n
        leftBdr = [None]*n

        stack = []
        for i in range(n-1, -1, -1):
            while len(stack)>0 and stack[-1]<=a[i]:
                stack.pop()

            rightBdr[i] = 0 if len(stack)==0 else stack[0]
            stack.append(a[i])

        stack = []
        for i in range(n):
            while len(stack)>0 and stack[-1]<=a[i]:
                stack.pop()

            leftBdr[i] = 0 if len(stack)==0 else stack[0]
            stack.append(a[i])
            
        total = 0
        for i in range(n):
            minBdr = min(rightBdr[i],leftBdr[i])
            total += max(0, minBdr-a[i])

        return total