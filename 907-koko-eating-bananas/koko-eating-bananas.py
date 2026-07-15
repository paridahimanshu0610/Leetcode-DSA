class Solution:
    def timeTaken(self, a, rate):
        totalTime = 0

        for e in a:
            if e % rate == 0:
                totalTime += e//rate
            else:
                totalTime += (e//rate)+1

        return totalTime
     
    def minEatingSpeed(self, a: List[int], hour: int) -> int:
        l, h = 1, max(a)

        while l <= h:
            mid = (l+h)//2
            time = self.timeTaken(a, mid)
            if time > hour:
                l = mid+1
            else:
                h = mid-1
        
        return l