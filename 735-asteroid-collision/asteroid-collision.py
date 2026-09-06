class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        n = len(a)
        stack = []

        for i in range(n):
            curr_exists = True
            while (a[i] < 0) and (len(stack) > 0) and stack[-1] > 0:
                if stack[-1] < abs(a[i]):
                    stack.pop()
                elif stack[-1] == abs(a[i]):
                    stack.pop()
                    curr_exists = False
                    break
                else:
                    curr_exists = False
                    break

            if curr_exists:
                stack.append(a[i])

        return stack 