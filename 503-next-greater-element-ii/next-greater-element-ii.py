class Solution:
    def nextGreaterElements(self, a: List[int]) -> List[int]:
        stack = []
        n = len(a)
        res = [None]*n

        for i in range(2*n-1, -1, -1):
            ii = i % n

            while len(stack) > 0 and stack[-1] <= a[ii]:
                stack.pop()
            if i < n:
                res[ii] = stack[-1] if len(stack) > 0 else -1
            stack.append(a[ii])

        return res