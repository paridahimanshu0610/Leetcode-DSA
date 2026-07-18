class Solution:
    def numIslands(self, a: List[List[str]]) -> int:
        m, n = len(a), len(a[0])
        visited = [[0]*n for _ in range(m)]

        def dfs(ii, jj):
            if (ii<0 or ii>=m) or (jj<0 or jj>=n) or a[ii][jj] == "0" or visited[ii][jj]:
                return

            visited[ii][jj] = 1

            for i,j in [(ii+1,jj), (ii-1,jj), (ii,jj+1), (ii,jj-1)]:
                dfs(i,j)            

        res = 0

        for i in range(m):
            for j in range(n):
                if (a[i][j] == "1") and not visited[i][j]:
                    res += 1
                    dfs(i, j)

        return res