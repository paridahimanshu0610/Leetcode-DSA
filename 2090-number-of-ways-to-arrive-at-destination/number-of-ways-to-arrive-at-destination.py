import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u,v,time in roads:
            adj[u].append((v,time))
            adj[v].append((u,time))

        numWays = [0]*n
        minDist = [float('inf')]*n

        minHeap = []
        heapq.heappush(minHeap, (0,0)) # Distance, node
        numWays[0] = 1
        minDist[0] = 0

        while len(minHeap) != 0:
            currDist, node = heapq.heappop(minHeap)

            if currDist > minDist[node]:
                continue

            for nv,time in adj[node]:
                tempDist = currDist+time

                if tempDist < minDist[nv]:
                    minDist[nv] = tempDist
                    numWays[nv] = numWays[node]
                    heapq.heappush(minHeap, (tempDist,nv))
                elif tempDist == minDist[nv]:
                    numWays[nv] = numWays[nv] + numWays[node]

        return numWays[n-1] % (10**9 + 7)