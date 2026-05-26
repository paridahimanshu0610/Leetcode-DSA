class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i0, j0 = -1, -1
        m, n = len(a), len(a[0])

        for i in range(m):
            for j in range(n):
                if a[i][j] == 0:
                    if i0 == -1:
                        i0, j0 = i, j
                    else:
                        a[i0][j], a[i][j0] = 0, 0
        
        if i0 == -1:
            return

        for i in range(m):
            if a[i][j0] == 0 and i != i0:
                for j in range(n):
                    a[i][j] = 0

        for j in range(n):
            if a[i0][j] == 0:
                for i in range(m):
                    a[i][j] = 0
        
        for j in range(n):
            a[i0][j] = 0