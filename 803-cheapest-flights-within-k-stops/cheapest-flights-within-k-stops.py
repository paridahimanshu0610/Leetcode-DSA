from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for frm,to,price in flights:
            adj[frm].append((to,price))

        q = deque()
        res = [float("inf")]*n
        q.append((0,src,0)) # nStops, node, price

        while len(q)!=0:
            currStops,node,currPrice = q.popleft()

            for nv,price in adj[node]:
                tempStops, tempPrice = currStops+1, currPrice+price
                if tempStops <= k+1 and tempPrice < res[nv]:
                    res[nv] = tempPrice
                    q.append((tempStops,nv,tempPrice))

        return -1 if res[dst] == float("inf") else res[dst]