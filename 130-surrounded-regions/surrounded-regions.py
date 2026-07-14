class Solution:
    def solve(self, a: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(a), len(a[0])
        visited = [[0]*n for _ in range(m)]

        def dfs(ii, jj):
            if (ii<0 or ii>=m) or (jj<0 or jj>=n):
                return

            if visited[ii][jj] or (a[ii][jj] == "X"):
                return

            if a[ii][jj] == "O":
                visited[ii][jj] = 1
                a[ii][jj] = "B"

            for i, j in [(ii+1,jj), (ii-1,jj), (ii,jj+1), (ii,jj-1)]:
                dfs(i, j) 

        for i in range(m):
            if (not visited[i][0]) and (a[i][0] == "O"):
                dfs(i, 0)

            if (not visited[i][n-1]) and (a[i][n-1] == "O"):
                dfs(i, n-1)

        for j in range(n):
            if (not visited[0][j]) and (a[0][j] == "O"):
                dfs(0, j)

            if (not visited[m-1][j]) and (a[m-1][j] == "O"):
                dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if a[i][j] == "B":
                    a[i][j] = "O"
                elif a[i][j] == "O":
                    a[i][j] = "X"