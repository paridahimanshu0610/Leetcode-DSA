class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = {i:0 for i in range(n)} # 0->unvisited, 1->visiting, 2->safe, 3->unsafe

        for i, edges in enumerate(graph):
            if len(edges) == 0:
                state[i] = 2

        def isSafe(curr):
            state[curr] = 1

            if state[curr] == 2:
                return True

            allSafe = True

            for nv in graph[curr]:
                if not state[nv]:
                    allSafe = allSafe and isSafe(nv)
                else:
                    allSafe = allSafe and (state[nv] == 2)

                if not allSafe:
                    state[curr] = 3
                    return False

            state[curr] = 2
            return True

        for i in range(n):
            if not state[i]:
                isSafe(i)

        return [key for key, value in state.items() if value==2]