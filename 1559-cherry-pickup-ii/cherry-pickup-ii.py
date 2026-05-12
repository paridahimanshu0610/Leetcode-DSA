class Solution:
    def totalFromCurrPointOnwards(self, a, i, j1, j2, dp):
        m, n = len(a), len(a[0])

        if (j1 < 0 or j1 >= n) or (j2 < 0 or j2 >= n):
            return -float('inf')

        if i == m-1:
            if j1 == j2:
                dp[i][j1][j2] = a[i][j1]
            else:
                dp[i][j1][j2] = a[i][j1] + a[i][j2]

            return dp[i][j1][j2]

        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        maxi = 0
        for dj1 in range(-1, 2):
            for dj2 in range(-1, 2):
                jj1, jj2 = j1+dj1, j2+dj2
                if j1 == j2:
                    maxi = max(maxi, a[i][j1] + self.totalFromCurrPointOnwards(a, i+1, jj1, jj2, dp))
                else:
                    maxi = max(maxi, a[i][j1] + a[i][j2] + self.totalFromCurrPointOnwards(a, i+1, jj1, jj2, dp))
        
        dp[i][j1][j2] = maxi

        return maxi

    def cherryPickup(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        dp = [[[-1]*n for _ in range(n)] for _ in range(m)]

        return self.totalFromCurrPointOnwards(a, 0, 0, n-1, dp)