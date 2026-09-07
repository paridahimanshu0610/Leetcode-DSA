class Solution:
    def subArrayRanges(self, a: List[int]) -> int:
        n = len(a)
        min_bound = [[None, None] for _ in range(n)]
        max_bound = [[None, None] for _ in range(n)]

        stack = []
        for i in range(n):
            while len(stack) > 0 and stack[-1][0] >= a[i]:
                _, idx = stack.pop() 
                min_bound[idx][1] = i-1
            
            stack.append([a[i], i])

        while len(stack) > 0:
            _, idx = stack.pop()
            min_bound[idx][1] = n-1

        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and stack[-1][0] > a[i]:
                _, idx = stack.pop() 
                min_bound[idx][0] = i+1
            
            stack.append([a[i], i])

        while len(stack) > 0:
            _, idx = stack.pop()
            min_bound[idx][0] = 0

        stack = []
        for i in range(n):
            while len(stack) > 0 and stack[-1][0] <= a[i]:
                _, idx = stack.pop() 
                max_bound[idx][1] = i-1
            
            stack.append([a[i], i])

        while len(stack) > 0:
            _, idx = stack.pop()
            max_bound[idx][1] = n-1

        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and stack[-1][0] < a[i]:
                _, idx = stack.pop() 
                max_bound[idx][0] = i+1
            
            stack.append([a[i], i])

        while len(stack) > 0:
            _, idx = stack.pop()
            max_bound[idx][0] = 0
        
        res = 0
        for i in range(n):
            n_min1, n_min2 = (i - min_bound[i][0]), (min_bound[i][1] - i)
            n_max1, n_max2 = (i - max_bound[i][0]), (max_bound[i][1] - i)

            res += a[i]*(n_max1 + n_max2 + n_max1*n_max2 + 1) - a[i]*(n_min1 + n_min2 + n_min1*n_min2 + 1)

        return res