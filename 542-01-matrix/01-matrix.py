from collections import deque

class Solution:
    def updateMatrix(self, a: List[List[int]]) -> List[List[int]]:
        m, n = len(a), len(a[0])
        q = deque()

        dist = [[None]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if a[i][j] == 0:
                    q.appendleft((i,j))
                    dist[i][j] = 0

        while len(q) != 0:
            (ii, jj) = q.pop()

            for i, j in [(ii+1,jj), (ii-1,jj), (ii,jj+1), (ii,jj-1)]:
                
                if ((i>=m) or (i<0)) or ((j>=n) or (j<0)):
                    continue
                
                if dist[i][j] is not None:
                    continue

                q.appendleft((i,j)) 
                dist[i][j] = 0 if a[i][j] == 0 else (dist[ii][jj] + 1)

        return dist