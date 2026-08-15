import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u,v,w in times:
            adj[u-1].append((v-1,w))
        
        minHeap = []
        heapq.heappush(minHeap, (0,k-1))
        res = [float('inf')]*n
        res[k-1] = 0

        while len(minHeap)!=0:
            currTime, node = heapq.heappop(minHeap)

            if currTime > res[node]:
                continue
            
            for nv,time in adj[node]:
                tempTime = currTime+time
                if tempTime < res[nv]:
                    res[nv] = tempTime
                    heapq.heappush(minHeap, (tempTime,nv))

        minTime = max(res)

        return -1 if minTime==float("inf") else minTime 