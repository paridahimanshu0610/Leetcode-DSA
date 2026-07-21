class Solution:
    def isBipartite(self, a: List[List[int]]) -> bool:
        status = {}
        
        def dfs(idx, connectedTo):
            currGroup = 'B' if connectedTo == 'A' else 'A'
            
            for node in a[idx]:
                if node in status:
                    if status[node] != currGroup:
                        return False
                    else:
                        continue
                else:
                    status[node] = currGroup
                    if not dfs(node, currGroup):
                        return False

            return True 
        
        for i in range(len(a)):
            if i in status:
                continue

            status[i] = 'A'
            if not dfs(i, 'A'):
                return False

        return True