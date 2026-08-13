import heapq

class Solution:
    def minimumEffortPath(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0]) 
        effort = [[float('inf')]*n for _ in range(m)]
        minHeap = []

        heapq.heappush(minHeap, (0, 0, 0))
        effort[0][0] = 0
        DIRS = [(1,0), (0,1), (-1,0), (0,-1)]

        while len(minHeap)!=0:
            currEffort, i, j = heapq.heappop(minHeap)

            if currEffort > effort[i][j]:
                continue

            for di,dj in DIRS:
                ii, jj = i+di, j+dj
                if (0 <= ii < m) and (0 <= jj < n):
                    tempEffort = max(abs(a[ii][jj]-a[i][j]), currEffort)
                    if tempEffort < effort[ii][jj]:
                        effort[ii][jj] = tempEffort
                        heapq.heappush(minHeap, (tempEffort,ii,jj))

        return effort[m-1][n-1] 