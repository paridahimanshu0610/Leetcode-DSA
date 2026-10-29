import heapq

class Solution:
    def getOrder(self, a: list[list[int]]) -> list[int]:
        n = len(a)
        b = [a[i]+[i] for i in range(n)]
        b.sort()

        currTime = 1
        i = 0
        queue = []
        res = []

        while len(res) < n:
            while i < n and currTime >= b[i][0]:
                heapq.heappush(queue, (b[i][1], b[i][2], b[i][0]))
                i += 1
            
            if len(queue) > 0:
                pTime, idx, _ = heapq.heappop(queue)
                currTime += pTime
                res.append(idx)
            else:
                currTime = b[i][0]

        return res