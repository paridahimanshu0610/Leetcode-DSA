from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, a: List[List[int]]) -> int:
        n = len(a)

        if a[n-1][n-1] == 1 or a[0][0] == 1:
            return -1
        elif n==1 and a[0][0] == 0:
            return 1

        dist = [[-1]*n for _ in range(n)]
        q = deque()

        q.appendleft(((0,0), 0))
        dist[0][0] = 0

        res = float('inf')

        while len(q) != 0:
            (i,j), currDist = q.pop()
            all_dirs = [(i+1,j), (i-1,j), (i,j+1), (i,j-1), (i-1,j-1), (i+1,j+1), (i-1,j+1), (i+1,j-1)]

            for ii, jj in all_dirs:
                if (0 <= ii < n) and (0 <= jj < n) and dist[ii][jj]==-1:
                    if a[ii][jj] == 0:
                        # print(f"For (i,j) = ({i},{j}):", ((ii,jj), currDist+1))
                        q.appendleft(((ii,jj), currDist+1))
                        dist[ii][jj] = currDist+1
                        res = min(res, currDist+1) if (ii==n-1 and jj==n-1) else res
                    else:
                        dist[ii][jj] = float('inf')

        if res == float("inf"):
            return -1
        else:
            return res+1
                        
