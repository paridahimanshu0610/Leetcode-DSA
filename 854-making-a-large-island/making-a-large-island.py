class Solution:
    def largestIsland(self, a: List[List[int]]) -> int:
        n = len(a)
        parent = [i for i in range(n*n)]
        size = [1 for _ in range(n*n)]

        def findUltimateParent(node):
            if node == parent[node]:
                return node
            parent[node] = findUltimateParent(parent[node])
            return parent[node]

        def unionBySize(u, v):
            pu, pv = findUltimateParent(u), findUltimateParent(v)

            if pu == pv:
                return 
                
            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]

        for i in range(n):
            for j in range(n):
                idx0 = i + n*j
                if a[i][j] == 0:
                    continue

                neighbours = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

                for ii, jj in neighbours:
                    idx1 = ii + n*jj
                    if (ii < 0) or (ii >= n) or (jj < 0) or (jj >= n) or (a[ii][jj] == 0):
                        continue

                    unionBySize(idx0, idx1)
        
        res = -1
        for i in range(n*n):
            pi = findUltimateParent(i)
            res = max(res, size[pi])

        for i in range(n):
            for j in range(n):
                if a[i][j] == 0:
                    neighbours = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                    tempSet = set()
                    tempSize = 1

                    for ii, jj in neighbours:
                        idx1 = ii + n*jj
                        if (ii < 0) or (ii >= n) or (jj < 0) or (jj >= n) or (a[ii][jj] == 0):
                            continue
                        pnv = findUltimateParent(idx1)
                        if pnv not in tempSet:
                            tempSet.add(pnv)
                            tempSize += size[pnv]
                    
                    res = max(res, tempSize)

        return res