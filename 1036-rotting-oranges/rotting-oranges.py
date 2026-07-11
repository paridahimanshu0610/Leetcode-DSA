from collections import deque

class Solution:
    def spread(self, a, i, j, q):
        l, r, t, b = j-1, j+1, i-1, i+1
        didSpread = False

        if l >= 0 and a[i][l] == 1:
            a[i][l] = 2
            q.appendleft((i,l))
            didSpread = True

        if t >= 0 and a[t][j] == 1:
            a[t][j] = 2
            q.appendleft((t,j))
            didSpread = True

        if r < len(a[0]) and a[i][r] == 1:
            a[i][r] = 2
            q.appendleft((i,r))
            didSpread = True

        if b < len(a) and a[b][j] == 1:
            a[b][j] = 2
            q.appendleft((b,j))
            didSpread = True

        return didSpread

    def orangesRotting(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])  
        q = deque()
        # visited = [[0]*n for _ in range(m)]

        currTime = 0

        for i in range(m):
            for j in range(n):
                if a[i][j] == 2:
                    q.appendleft((i,j))

        while len(q)!=0:
            currLen = len(q)
            didSpread = False

            for _ in range(currLen):
                (i, j) = q.pop()
                if self.spread(a, i, j, q):
                    didSpread = True

            if didSpread:
                currTime += 1

        for i in range(m):
            for j in range(n):
                if a[i][j] == 1:
                    return -1

        return currTime