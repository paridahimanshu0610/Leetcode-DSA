class Solution:
    def search(self, a: List[int], x: int) -> int:
        n = len(a)
        l, h = 0, n-1

        while l <= h:
            mid = (l + h) // 2
            if x == a[mid]:
                return mid
            elif a[mid] <= a[h]:
                if (a[mid] < x <= a[h]):
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                if (a[l] <= x < a[mid]):
                    h = mid - 1
                else:
                    l = mid + 1

        return -1