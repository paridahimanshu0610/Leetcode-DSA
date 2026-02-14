class Solution:
    def max_cherry(self, a, i, j1, j2, dp):
        if i==len(a)-1 and (0<=j1<len(a[0])) and (0<=j2<len(a[0])):
            if j1==j2:
                dp[i][j1][j2] = a[i][j1]
            else:
                dp[i][j1][j2] = a[i][j1] + a[i][j2]

        if (i>=len(a)) or (j1<0 or j1>=len(a[0])) or (j2<0 or j2>=len(a[0])):
            return float('-inf')

        if dp[i][j1][j2]!=-1:
            return dp[i][j1][j2]

        nxt_state_max_gain = float('-inf')
        for dj1 in range(-1,2,1):
            for dj2 in range(-1,2,1):
                nxt_state_max_gain = max(nxt_state_max_gain, self.max_cherry(a, i+1, j1+dj1, j2+dj2, dp))
        curr_state_gain = a[i][j1] + a[i][j2] if j1!=j2 else a[i][j1]

        dp[i][j1][j2] = curr_state_gain + nxt_state_max_gain 

        return dp[i][j1][j2]

    def cherryPickup(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        dp = [[[-1]*n for _ in range(n)] for _ in range(m)]
        
        for j1 in range(n):
            for j2 in range(n):
                dp[m-1][j1][j2] = a[m-1][j1] if j1==j2 else (a[m-1][j1] + a[m-1][j2])

        for i in range(m-2, -1, -1):
            for j1 in range(n):
                for j2 in range(n):
                    curr_state_gain = a[i][j1] + a[i][j2] if j1!=j2 else a[i][j1]
                    nxt_state_max_gain = float('-inf')
                    for dj1 in range(-1,2,1):
                        for dj2 in range(-1,2,1):
                            if (j1+dj1<0 or j1+dj1>=n) or (j2+dj2<0 or j2+dj2>=n):
                                continue
                            nxt_state_max_gain = max(nxt_state_max_gain, dp[i+1][j1+dj1][j2+dj2])
                    dp[i][j1][j2] = curr_state_gain + nxt_state_max_gain                 

        return dp[0][0][n-1]    