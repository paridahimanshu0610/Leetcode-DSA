class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        graph = defaultdict(list)

        row_groups = defaultdict(list)
        col_groups = defaultdict(list)

        for i, (x, y) in enumerate(stones):
            row_groups[x].append(i)
            col_groups[y].append(i)

        # Chain stones sharing the same row
        for group in row_groups.values():
            for i in range(len(group) - 1):
                u, v = group[i], group[i+1]
                graph[u].append(v)
                graph[v].append(u)

        # Chain stones sharing the same column
        for group in col_groups.values():
            for i in range(len(group) - 1):
                u, v = group[i], group[i+1]
                graph[u].append(v)
                graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1

        return n - components