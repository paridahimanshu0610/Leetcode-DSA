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

        dp = [[[None]*n for _ in range(n)] for _ in range(m)]

        maxi = -float('inf')

        for j1 in range(n):
            for j2 in range(n):
                maxi = max(maxi, self.soFar(a, m-1, j1, j2, dp))

        return maxi