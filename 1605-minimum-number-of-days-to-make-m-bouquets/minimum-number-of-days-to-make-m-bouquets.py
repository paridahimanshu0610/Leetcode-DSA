class Solution:
    def numBouquets(self, a, waitDays, k):
        currCnt = 0
        totalBouquets = 0

        for i in range(len(a)):
            if a[i] <= waitDays:
                currCnt += 1
            else:
                currCnt = 0

            if currCnt == k:
                totalBouquets += 1
                currCnt = 0

        return totalBouquets 

    def minDays(self, a: List[int], m: int, k: int) -> int:
        n = len(a)

        if n//k < m:
            return -1

        l, h = 1, max(a)

        while l <= h:
            mid = (l+h)//2

            totalBouquets = self.numBouquets(a, mid, k)

            if totalBouquets >= m:
                h = mid-1
            else:
                l = mid+1

        return l 