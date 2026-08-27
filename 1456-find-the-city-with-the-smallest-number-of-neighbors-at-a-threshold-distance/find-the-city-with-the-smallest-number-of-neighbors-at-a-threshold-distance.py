class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        maxDist = float('inf')
        adj = [[maxDist]*n for _ in range(n)]

        for u,v,wt in edges:
            adj[u][v] = wt
            adj[v][u] = wt

        for i in range(n):
            adj[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i==k or j==k:
                        continue

                    if (adj[i][j] == maxDist) and (adj[i][k] == maxDist or adj[k][j] == maxDist):
                        continue

                    tempDist = adj[i][k] + adj[k][j]

                    if tempDist < adj[i][j]:
                        adj[i][j] = tempDist

        minCnt, resIdx = float("inf"), -1

        print(adj)

        for i in range(n):
            cnt = 0
            for j in range(n):
                if i == j:
                    continue

                if adj[i][j] <= distanceThreshold:
                    cnt += 1

            if cnt <= minCnt:
                minCnt = cnt
                resIdx = i

        return resIdx