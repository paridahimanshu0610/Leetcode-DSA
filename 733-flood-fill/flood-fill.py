from collections import deque

class Solution:
    def inRange(self, i, j, m, n):
        return (0 <= i < m) and (0 <= j < n)

    def floodFill(self, a: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(a), len(a[0])
        visited = [[0]*n for _ in range(m)]

        dq = deque()
        dq.appendleft((sr, sc))
        visited[sr][sc] = 1
        val = a[sr][sc]
        a[sr][sc] = color

        while len(dq) != 0:
            curr_size = len(dq)

            print(dq)
            for _ in range(curr_size):
                i, j = dq.pop()
                neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

                # Neighbours of current item
                for x, y in neighbours:
                    if self.inRange(x, y, m, n) and (a[x][y] == val) and (not visited[x][y]):
                        a[x][y] = color
                        visited[x][y] = 1
                        dq.appendleft((x, y))

        return a