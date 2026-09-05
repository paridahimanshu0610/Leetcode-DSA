class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        size = [1]*n
        parent = [i for i in range(n)]

        def findUltimateParent(u):
            if parent[u] == u:
                return u
            parent[u] = findUltimateParent(parent[u])
            return parent[u]

        def shareSameUltimateParent(u, v):
            return findUltimateParent(u) == findUltimateParent(v)

        def unionBySize(u,v):
            pu, pv = findUltimateParent(u), findUltimateParent(v)

            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]

        spare = 0
        for u, v in connections:
            if shareSameUltimateParent(u, v): 
                spare += 1
                continue

            unionBySize(u,v)
        
        for i in range(n):
            findUltimateParent(i)
            
        distinct_parents = set(parent)

        return len(distinct_parents)-1 if len(distinct_parents)-1 <= spare else -1   