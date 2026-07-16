class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        n = len(a)
        l, h = 0, n-1

        while l <= h:
            mid = (l+h)//2
            currMissing = a[mid] - (mid+1)

            if currMissing >= k:
                h = mid-1
            else:
                l = mid+1
        
        if h < 0:
            return k
        else:
            currMissing = a[h] - (h+1)
            return a[h] + (k-currMissing)