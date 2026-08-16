import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u,v,time in roads:
            adj[u].append((v,time))
            adj[v].append((u,time))
        
        minHeap = []
        heapq.heappush(minHeap, (0,0)) # dist from 0, node
        
        res = [(float('inf'))]*n
        ways = [0]*n
        res[0] = 0
        ways[0] = 1
 
        while len(minHeap)!=0:
            currTime, node = heapq.heappop(minHeap)

            if currTime > res[node]:
                continue

            if node == n-1:
                continue
            
            for nv,time in adj[node]:
                tempTime = currTime+time            
                
                if (tempTime < res[nv]):
                    res[nv] = tempTime
                    ways[nv] = ways[node]
                    heapq.heappush(minHeap, (tempTime,nv))
                elif (tempTime == res[nv]):
                    ways[nv] = ways[nv]+ways[node]               

        return ways[n-1] % (10**9 + 7)