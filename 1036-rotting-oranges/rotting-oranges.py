from collections import deque

class Solution:
    def checkAllRotten(self, grid):
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return False
        
        return True

    def inRange(self, i, j, m, n):
        return (0 <= i < m) and (0 <= j < n)
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        time = 0
        dq = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    visited[i][j] = 1
                    dq.appendleft((i, j))

        time = 0
        while len(dq) != 0:
            curr_size = len(dq)
            found_rotten_neighbours = False

            # Oranges currently rotten
            for _ in range(curr_size):
                i, j = dq.pop()
                neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for x, y in neighbours:
                    if self.inRange(x, y, m, n) and (grid[x][y] == 1) and (not visited[x][y]):
                        found_rotten_neighbours = True
                        dq.appendleft((x, y))
                        grid[x][y] = 2    
                        visited[x][y] = 1            

            if found_rotten_neighbours:
                time += 1

        if self.checkAllRotten(grid):
            return time
        else:
            return -1