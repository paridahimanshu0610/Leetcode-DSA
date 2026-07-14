class Solution:
    def solve(self, a: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(a), len(a[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if a[i][j] != "O":
                return
            a[i][j] = "S"  # mark safe
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # 1. Run DFS from every border 'O' to mark safe regions
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        # 2. Flip remaining O -> X, and restore S -> O
        for i in range(m):
            for j in range(n):
                if a[i][j] == "O":
                    a[i][j] = "X"
                elif a[i][j] == "S":
                    a[i][j] = "O"