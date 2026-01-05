class Solution:
    def getDays(self, a, cap):
        daysTaken = 0
        currLoad = 0
        i = 0

        while i < len(a):
            currLoad += a[i]
            if currLoad > cap:
                daysTaken += 1
                currLoad = a[i]
            elif currLoad == cap:
                daysTaken += 1
                currLoad = 0
            i += 1

        if currLoad > 0:
            daysTaken += 1

        return daysTaken

    def shipWithinDays(self, a: List[int], daysAvailable: int) -> int:
        l, h = 0, 0

        for e in a:
            l = max(l, e)
            h += e

        while l <= h:
            mid = (l+h)//2
            daysRequired = self.getDays(a, mid)

            if daysRequired <= daysAvailable:
                h = mid-1
            else:
                l = mid+1
        
        return l