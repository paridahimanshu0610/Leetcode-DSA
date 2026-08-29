class Solution:
    def nextGreaterElements(self, a: List[int]) -> List[int]:
        stack = []
        n = len(a)
        res = [None]*n

        for i in range(2*n-1, -1, -1):
            curr_i = i % n
            while len(stack) > 0 and stack[-1] <= a[curr_i]:
                stack.pop()

            if i < n:    
                if len(stack) > 0:
                    res[i] = stack[-1] # Here, curr_i = i
                else:
                    res[i] = -1

            stack.append(a[curr_i])

        return res