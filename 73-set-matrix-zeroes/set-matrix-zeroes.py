class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x, y = None, None

        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j]==0:  
                    if x is None:
                        x, y = i, j
                    else:
                        a[x][j], a[i][y] = 0, 0
        
        if x is None:
            return

        for i in range(len(a)):
            if i==x:
                continue
            if a[i][y]==0:
                for j in range(len(a[0])):
                    a[i][j] = 0

        for j in range(len(a[0])):
            # No longer required
            # if j==y:
            #     continue
            if a[x][j]==0:
                for i in range(len(a)):
                    a[i][j] = 0
        
        for i in range(len(a)):
            a[i][y] = 0
        
        for j in range(len(a[0])):
            a[x][j] = 0