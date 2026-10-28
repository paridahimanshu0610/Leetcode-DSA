import heapq

class MedianFinder:
    def __init__(self):
        self.maxHp = [] # Left-half
        self.minHp = [] # Right-half

    def addNum(self, num: int) -> None:
        if len(self.maxHp) > 0 and num <= -self.maxHp[0]:
            heapq.heappush(self.maxHp, -num)
        else:
            heapq.heappush(self.minHp, num)

        while abs(len(self.maxHp)-len(self.minHp)) > 1:
            if len(self.maxHp) > len(self.minHp):
                heapq.heappush(self.minHp, -heapq.heappop(self.maxHp))
            else:
                heapq.heappush(self.maxHp, -heapq.heappop(self.minHp))

        # print(num, self.maxHp, self.minHp)

    def findMedian(self) -> float:
        if len(self.minHp) == 0 and len(self.maxHp) == 0:
            return -1

        if len(self.minHp) - len(self.maxHp) == 0:
            return round((self.minHp[0]+(-self.maxHp[0]))/2, 5)
        elif len(self.minHp) == 0:
            return -self.maxHp[0]
        elif len(self.maxHp) == 0:
            return self.minHp[0]
        else:
            return -self.maxHp[0] if len(self.maxHp) > len(self.minHp) else self.minHp[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()