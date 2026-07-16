class Solution:
    def numEnclaves(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])

        visited = [[0]*n for _ in range(m)]
        
        def dfs(ii, jj):
            if ((ii<0 or ii>=m) or (jj<0 or jj>=n)) or visited[ii][jj] or (a[ii][jj] == 0):
                return

            visited[ii][jj] = 1 

            for i, j in [(ii+1,jj), (ii-1,jj), (ii,jj+1), (ii,jj-1)]:
                dfs(i, j)

        for i in range(m):
            if (a[i][0] == 1) and not visited[i][0]:
                dfs(i, 0)

            if (a[i][n-1] == 1) and not visited[i][n-1]:
                dfs(i, n-1)

        for j in range(n):
            if (a[0][j] == 1) and not visited[0][j]:
                dfs(0, j)

            if (a[m-1][j] == 1) and not visited[m-1][j]:
                dfs(m-1, j)
        
        cnt = 0

        for i in range(m):
            for j in range(n):
                if a[i][j] == 1 and not visited[i][j]:
                    cnt += 1

        return cnt