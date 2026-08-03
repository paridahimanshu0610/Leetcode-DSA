class Solution:
    def searchMatrix(self, a: List[List[int]], x: int) -> bool:
        m, n = len(a), len(a[0])

        def getPos(pos):
            return pos//n, pos%n

        l, h = 0, m*n-1

        while l <= h:
            mid = (l+h)//2
            i, j = getPos(mid)

            if a[i][j] > x:
                h = mid-1
            elif a[i][j] < x:
                l = mid+1
            else:
                return True

        return False