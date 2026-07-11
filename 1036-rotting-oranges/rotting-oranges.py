class Solution:
    def spread(self, a, i, j, rotAt, currTime):
        l, r, t, b = j-1, j+1, i-1, i+1
        didSpread = False

        if l >= 0 and a[i][l] == 1:
            rotAt[i][l] = currTime+1 
            a[i][l] = 2
            didSpread = True

        if t >= 0 and a[t][j] == 1:
            rotAt[t][j] = currTime+1 
            a[t][j] = 2
            didSpread = True

        if r < len(a[0]) and a[i][r] == 1:
            rotAt[i][r] = currTime+1 
            a[i][r] = 2
            didSpread = True

        if b < len(a) and a[b][j] == 1:
            rotAt[b][j] = currTime+1 
            a[b][j] = 2
            didSpread = True

        return didSpread

    def orangesRotting(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        rotAt = [[0]*n for _ in range(m)]
        currTime = 0
        found = True
        didSpread = True

        while found and didSpread:

            found = False
            didSpread = False
            for i in range(m):
                for j in range(n):
                    if a[i][j] == 2 and rotAt[i][j] == currTime:
                        found = True
                        if self.spread(a, i, j, rotAt, currTime):
                            didSpread = True
            
            if found and didSpread:
                currTime += 1

        for i in range(m):
            for j in range(n):
                if a[i][j] == 1:
                    return -1

        return currTime