class Solution:
    def days(self, a, shipCap):
        cnt = 0
        currLoad = 0

        for i in range(len(a)):
            currLoad += a[i]

            if currLoad < shipCap:
                continue
            elif currLoad == shipCap:
                cnt += 1
                currLoad = 0
            else:
                cnt += 1
                currLoad = a[i]
        
        if currLoad > 0:
            cnt += 1
        
        return cnt

    def shipWithinDays(self, a: List[int], targetDays: int) -> int:
        l, h = float('-inf'), 0

        for i in range(len(a)):
            if a[i] > l:
                l = a[i]
            h += a[i]

        while l <= h:
            mid = (l+h)//2
            currDaysTaken = self.days(a, mid)

            if currDaysTaken <= targetDays:
                h = mid-1
            else:
                l = mid+1

        return l