class Solution:
    def search(self, a: List[int], x: int) -> bool:
        n = len(a)
        l, h = 0, n-1

        while l <= h:
            mid = (l + h) // 2
            if x == a[mid]:
                return True
            elif a[l] == a[mid] == a[h]:
                l += 1
                h -= 1
                continue
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

        return False