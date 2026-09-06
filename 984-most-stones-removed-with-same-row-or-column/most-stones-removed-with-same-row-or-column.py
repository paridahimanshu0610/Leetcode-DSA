class Solution:
    def removeStones(self, a: List[List[int]]) -> int:
        edges = []
        n = len(a)

        parent = {}
        size = {}

        def findUltimateParent(node):
            if parent.get(node, None) is None:
                parent[node] = node
                return node
            elif parent[node] == node:
                return node

            parent[node] = findUltimateParent(parent[node])

            return parent[node]

        def shareSameParent(u,v):
            return findUltimateParent(u) == findUltimateParent(v)

        def unionBySize(u, v):
            pu, pv = findUltimateParent(u), findUltimateParent(v)

            if size.get(pu,1) < size.get(pv,1):
                parent[pu] = pv
                if pv in size:
                    size[pv] += size.get(pu,1)
                else:
                    size[pv] = 1+size.get(pu,1)                    
            else:
                parent[pv] = pu
                if pu in size:
                    size[pu] += size.get(pv,1)
                else:
                    size[pu] = 1+size.get(pv,1)  

        for x,y in a:
            if shareSameParent(x, ~y):
                continue

            unionBySize(x, ~y)

        unique_parents = {findUltimateParent(node) for node in parent.keys()}

        return n-len(unique_parents)