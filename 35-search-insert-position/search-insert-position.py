class Solution:
    def searchInsert(self, a: List[int], target: int) -> int:
        n = len(a)
        l, h = 0, n-1

        while l <= h:
            mid = (l+h)//2
            if a[mid] == target:
                return mid
            elif target > a[mid]:
                l = mid+1
            else:
                h = mid-1

        return l