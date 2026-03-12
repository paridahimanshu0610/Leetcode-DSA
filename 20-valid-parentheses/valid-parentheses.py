class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        match_braces = {'(':')', '{':'}', '[':']'}

        for c in s:
            if c in '([{':
                my_stack.append(c)
            else:
                if len(my_stack) == 0:
                    return False
                    
                top = my_stack.pop()
                if match_braces[top] != c:
                    return False

        return len(my_stack) == 0 