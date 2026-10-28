import heapq

class Solution:
    def topKFrequent(self, a: list[int], k: int) -> list[int]:
        freq = {}
        for e in a:
            if e not in freq:
                freq[e] = -1
            else:
                freq[e] -= 1
        
        heap = [(val, key) for key, val in freq.items()]
        heapq.heapify(heap)

        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res