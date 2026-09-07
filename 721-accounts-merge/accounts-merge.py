class Solution:
    def accountsMerge(self, acc: List[List[str]]) -> List[List[str]]:
        n = len(acc)
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        email_idx = {}

        def findUltimateParent(node):
            if node == parent[node]:
                return node
            parent[node] = findUltimateParent(parent[node])
            return parent[node]

        def unionBySize(pu, pv):
            if size[pu] < size[pv]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]

        for i in range(n):
            for j in range(1, len(acc[i])):
                if acc[i][j] in email_idx:
                    ult_parent_1 = findUltimateParent(email_idx[acc[i][j]])
                    ult_parent_2 = findUltimateParent(i)
                    unionBySize(ult_parent_1, ult_parent_2)
                else:
                    email_idx[acc[i][j]] = i

        res = {}

        for email, idx in email_idx.items():
            parent[idx] = findUltimateParent(idx)

            if parent[idx] in res:
                res[parent[idx]].append(email)
            else:
                res[parent[idx]] = [email]

        return [[acc[key][0]] + sorted(list(value)) for key, value in res.items()]