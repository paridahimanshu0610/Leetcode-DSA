class Solution:
    def get_expr_boundary(self, a, idx):
        if (a[idx] == "t") or (a[idx] == "f"):
            return idx 
        
        stack = ['(']
        idx += 2

        while idx < len(a) and len(stack) != 0:
            if a[idx] == "(":
                stack.append("(")
            elif a[idx] == ")":
                stack.pop()
            
            idx += 1

        return idx-1

    def eval(self, a, l, h):
        if l == h:
            return a[l] == "t"

        # if dp[l][h] is not None:
        #     return dp[l][h]

        if a[l] == "!":
            op = lambda x1, x2: not x2
            curr = True
        elif a[l] == "&":
            op = lambda x1, x2: x1 and x2
            curr = True
        else:
            op = lambda x1, x2: x1 or x2
            curr = False
        
        i = l+2
        while i < h:
            temp_l = i
            temp_h = self.get_expr_boundary(a, temp_l)
            curr = op(curr, self.eval(a, temp_l, temp_h))
            i = temp_h + 2

        # dp[l][h] = curr

        return curr

    def parseBoolExpr(self, a: str) -> bool:
        n = len(a)
        # dp = [[None]*n for _ in range(n)]

        return self.eval(a, 0, n-1)