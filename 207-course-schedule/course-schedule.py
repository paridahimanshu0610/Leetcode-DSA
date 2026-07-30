class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        a = [[] for _ in range(n)]

        for c1, c2 in prerequisites:
            a[c2].append(c1)

        visited = [0]*n

        def detectCycle(curr):
            visited[curr] = 1

            for nv in a[curr]:
                if not visited[nv] and detectCycle(nv):
                    return True
                elif visited[nv] == 1:
                    return True

            visited[curr] = 2

            return False

        for i in range(n):
            if not visited[i] and detectCycle(i):
                return False

        return True