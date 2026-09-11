class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        ctr = k

        for e in num:
            while len(stack) > 0 and int(stack[-1]) > int(e) and ctr > 0:
                stack.pop()
                ctr -= 1
            stack.append(e)
        
        while len(stack) > 0 and ctr > 0:
            stack.pop()
            ctr -= 1

        res = []
        while len(stack) > 0:
            res.append(stack.pop())

        i = len(res)-1
        while i >= 0 and res[i] == "0":
            res.pop()
            i -= 1

        n = len(res)
        for i in range(n//2):
            res[i], res[n-1-i] = res[n-1-i], res[i]

        return "0" if len(res)==0 else "".join(res)

