import heapq

class Solution:
    def isNStraightHand(self, a: list[int], size: int) -> bool:
        n = len(a)
        if n % size != 0:
            return False

        cntDict = {}
        for e in a:
            cntDict[e] = 1 if e not in cntDict else cntDict[e] + 1 
        
        heap = list(cntDict.keys())
        heapq.heapify(heap)

        def decr(key):
            if key in cntDict:
                cntDict[key] -= 1
                if cntDict[key] == 0:
                    del cntDict[key]

        for i in range(n//size):
            curr = heapq.heappop(heap)
            while (curr not in cntDict) and (len(heap)>0):
                curr = heapq.heappop(heap)

            decr(curr)
            if curr in cntDict:
                heapq.heappush(heap, curr)

            curr = curr+1
            for j in range(size-1):
                if curr not in cntDict:
                    return False
                decr(curr)
                curr = curr+1 

        return True 