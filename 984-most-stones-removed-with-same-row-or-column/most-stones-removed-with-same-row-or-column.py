class Solution:
    def removeStones(self, a: List[List[int]]) -> int:
        edges = []
        n = len(a)

        for i in range(n):
            x0, y0 = a[i]
            for j in range(i+1, n):
                x1, y1 = a[j]
                if x0==x1 or y0==y1:
                    edges.append([i,j])

        parent = [i for i in range(n)]
        size = [1 for i in range(n)]

        def findUltimateParent(node):
            if node == parent[node]:
                return node
            parent[node] = findUltimateParent(parent[node])
            return parent[node]

        def shareSameParent(u,v):
            return findUltimateParent(u) == findUltimateParent(v)

        def unionBySize(u, v):
            pu, pv = findUltimateParent(u), findUltimateParent(v)

            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]

        for u,v in edges:
            if shareSameParent(u,v):
                continue

            unionBySize(u,v)

        res = 0
        for i in range(n):
            if i != parent[i]:
                res += 1

        return res