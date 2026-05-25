class Solution:
    def soFar(self, a, r, c1, c2, dp):
        n = len(a[0])

        if r < 0 or (c1 < 0 or c1 >= n) or (c2 < 0 or c2 >= n):
            return -float('inf')
        
        if r == 0:
            if c1 == 0 and c2 == n-1:
                dp[0][c1][c2] = a[0][c1] + a[0][c2]
            else:
                dp[0][c1][c2] = -float('inf')
            
            return dp[0][c1][c2]

        if dp[r][c1][c2] is not None:
            return dp[r][c1][c2]

        maxi = -float('inf')

        for j1 in range(c1-1, c1+2):
            for j2 in range(c2-1, c2+2):
                if (j1 < 0 or j1 >= n) or (j2 < 0 or j2 >= n):
                    continue
                maxi = max(maxi, self.soFar(a, r-1, j1, j2, dp))
        
        maxi = a[r][c1] + maxi if c1 == c2 else a[r][c1] + a[r][c2] + maxi
        dp[r][c1][c2] = maxi

        return maxi

    def cherryPickup(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])

        dp = [[-float('inf')]*n for _ in range(n)]
        dp[0][n-1] = a[0][0] + a[0][n-1]

        for r in range(1, m):
            temp = [[None]*n for _ in range(n)]

            for c1 in range(n):
                for c2 in range(n):

                    maxi = -float('inf')
                    for j1 in range(c1-1, c1+2):
                        for j2 in range(c2-1, c2+2):
                            if (j1 < 0 or j1 >= n) or (j2 < 0 or j2 >= n):
                                continue
                            maxi = max(maxi, dp[j1][j2])
                    
                    maxi = a[r][c1] + maxi if c1 == c2 else a[r][c1] + a[r][c2] + maxi
                    temp[c1][c2] = maxi

            dp = temp                  

        maxi = -float('inf')
        for c1 in range(n):
            for c2 in range(n):
                maxi = max(maxi, dp[c1][c2])
                
        return maxi