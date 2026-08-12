from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, a: List[List[int]]) -> int:
        n = len(a)

        if a[n-1][n-1] == 1 or a[0][0] == 1:
            return -1
        elif n==1 and a[0][0] == 0:
            return 1

        visited = [[0]*n for _ in range(n)]
        q = deque()

        q.append(((0,0), 0))
        visited[0][0] = 1

        DIRS = [(1,0), (0,1), (-1,0), (0,-1), (-1,-1), (1,1), (-1,1), (1,-1)]

        while len(q) != 0:
            (i,j), currDist = q.popleft()

            for di, dj in DIRS:
                ii, jj = i+di, j+dj
                if (0 <= ii < n) and (0 <= jj < n) and not visited[ii][jj]:
                    visited[ii][jj] = 1

                    if a[ii][jj] == 0:
                        q.append(((ii,jj), currDist+1))
                    
                    if ii==n-1 and jj==n-1:
                        return currDist+2

        return -1