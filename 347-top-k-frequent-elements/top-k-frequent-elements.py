import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, a: list[int], k: int) -> list[int]:
        # TC: O(n), SC: O(m+k) -> O(m) since k <= m
        freq = Counter(a)
        heap = []

        # TC: O(m log(k))
        for key, val in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            elif val > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (val, key))

        return [item[1] for item in heap]