class Solution:
    def max_cherries(self, a, i, j1, j2, dp):
        if (i==len(a)-1) and (0 <= j1 < len(a[0])) and (0 <= j2 < len(a[0])):
            if j1==j2:
                dp[i][j1][j2] = a[i][j1]
            else:
                dp[i][j1][j2] = a[i][j1] + a[i][j2]         
            
            return dp[i][j1][j2]

        if (i >= len(a)) or (j1 < 0 or j1 >= len(a[0])) or (j2 < 0 or j2 >= len(a[0])):
            return float('-inf')
        
        if dp[i][j1][j2]!=-1:
            return dp[i][j1][j2]
        
        max_res = 0
        curr_cherry = a[i][j1] if j1==j2 else a[i][j1] + a[i][j2]
        for dj1 in range(-1,2,1):
            for dj2 in range(-1,2,1):
                max_res = max(max_res, self.max_cherries(a, i+1, j1+dj1, j2+dj2, dp))    
        dp[i][j1][j2] = curr_cherry + max_res

        return dp[i][j1][j2]

    def cherryPickup(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        dp = [[[-1]*n for _ in range(n)] for _ in range(m)]

        return self.max_cherries(a, 0, 0, n-1, dp)
        