class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        n = len(a)
        l, h = 0, n-1

        while l <= h:
            mid = (l+h)//2
            left = a[mid-1] if mid-1 >= 0 else -float('inf') 
            right = a[mid+1] if mid+1 < n else -float('inf')

            if (a[mid] > left) and (a[mid] > right):
                return mid
            elif (left < a[mid] < right):
                l = mid+1
            elif (left > a[mid] > right):
                h = mid-1
            else:
                l = mid+1

        return mid