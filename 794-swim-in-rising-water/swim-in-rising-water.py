import heapq

class Solution:
    def swimInWater(self, a: List[List[int]]) -> int:
        n = len(a)
        dist = [[float("inf")]*n for _ in range(n)]
        dist[0][0] = a[0][0]

        minHeap = []
        heapq.heappush(minHeap, (a[0][0], 0, 0))

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while len(minHeap) != 0:
            currTime, x, y = heapq.heappop(minHeap)

            if currTime > dist[x][y]:
                continue
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if (nx < 0 or nx >= n) or (ny < 0 or ny >= n):
                    continue
                
                timeTaken = max(currTime, a[nx][ny])
                if timeTaken < dist[nx][ny]:
                    dist[nx][ny] = timeTaken
                    heapq.heappush(minHeap, (timeTaken, nx, ny))

        return dist[n-1][n-1]