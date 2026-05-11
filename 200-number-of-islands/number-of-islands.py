class Solution:
    def inRange(self, i, j, m, n):
        return (0 <= i < m) and (0 <= j < n)
    
    def traverse(self, a, i, j, visited):
        visited[i][j] = 1
        neighbours = [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]

        for x, y in neighbours:
            if self.inRange(x, y, len(a), len(a[0])) and (a[x][y] == "1") and (not visited[x][y]):
                self.traverse(a, x, y, visited)

    def numIslands(self, a: List[List[str]]) -> int:
        m, n = len(a), len(a[0])
        visited = [[0]*n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                if (a[i][j] == "1") and (not visited[i][j]):
                    res += 1
                    self.traverse(a, i, j, visited)

        return res