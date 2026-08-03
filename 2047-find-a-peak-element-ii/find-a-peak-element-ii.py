class Solution:
    def findPeakGrid(self, a: List[List[int]]) -> List[int]:
        m, n = len(a), len(a[0])

        def findMaxRow(a, j):
            i_max = 0

            for i in range(m):
                if a[i][j] > a[i_max][j]:
                    i_max = i
            
            return i_max

        l, h = 0,  n-1
        while l <= h:
            mid = (l+h)//2
            i_max = findMaxRow(a, mid)

            curr = a[i_max][mid]
            right = a[i_max][mid+1] if mid <= n-2 else -1
            left = a[i_max][mid-1] if mid >= 1 else -1

            if curr < right:
                l = mid+1
            elif curr < left:
                h = mid-1
            else:
                return [i_max, mid]

        return [-1, -1]
