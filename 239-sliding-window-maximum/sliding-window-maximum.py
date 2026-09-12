from collections import deque

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        n = len(a)
        dll = deque()
        res = []

        for i in range(k):
            while len(dll) > 0 and a[i] >= dll[0][0]:
                dll.popleft()
            dll.appendleft((a[i], i))
        res.append(dll[-1][0])

        for i in range(k, n):
            while len(dll) > 0 and dll[-1][1] <= i-k:
                dll.pop()

            while len(dll) > 0 and a[i] >= dll[0][0]:
                dll.popleft()
            dll.appendleft((a[i], i))
            res.append(dll[-1][0])

        return res                 