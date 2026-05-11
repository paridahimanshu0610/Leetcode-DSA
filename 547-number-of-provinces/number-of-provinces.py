class Solution:
    def traverse(self, adj, node, visited):
        visited[node] = 1

        for e in adj[node]:
            if not visited[e]:
                self.traverse(adj, e, visited)

    def findCircleNum(self, a: List[List[int]]) -> int:
        n = len(a)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and a[i][j] == 1:
                    adj[i].append(j)

        visited = [0]*n
        res = 0

        for i in range(n):
            if not visited[i]:
                res += 1
                self.traverse(adj, i, visited)

        return res