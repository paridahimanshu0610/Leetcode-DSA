class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        termNodes = set()
        safeNode = {i:False for i in range(n)}

        for i, edges in enumerate(graph):
            if len(edges) == 0:
                termNodes.add(i)
                safeNode[i] = True

        visited = [0]*n

        def isSafe(curr):
            visited[curr] = 1

            if safeNode[i]:
                return True

            allSafe = True

            for nv in graph[curr]:
                if not visited[nv]:
                    allSafe = allSafe and isSafe(nv)
                else:
                    allSafe = allSafe and safeNode[nv]

                if not allSafe:
                    return False

            safeNode[curr] = True

            return True

        for i in range(n):
            if not visited[i]:
                isSafe(i)

        return [key for key, value in safeNode.items() if value]