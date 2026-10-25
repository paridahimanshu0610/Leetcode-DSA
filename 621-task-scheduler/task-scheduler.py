import heapq
from collections import deque

class Solution:
    def leastInterval(self, a: list[str], n: int) -> int:
        temp = {}

        for e in a:
            temp[e] = 1 if e not in temp else temp[e]+1 

        hp = []
        q = deque()
        for key, val in temp.items():
            heapq.heappush(hp, (-val,key))

        curr_ptr = 0
        # res = []

        while len(hp) != 0 or len(q) != 0:
            # Check the queue and add all items who have gone past their waiting time
            while len(q) > 0 and q[0][2] <= curr_ptr:
                temp = q.popleft()
                heapq.heappush(hp, (temp[0], temp[1]))

            if len(hp) > 0:
                cnt, key = heapq.heappop(hp)
                cnt = -cnt

                if cnt-1 > 0:
                    q.append((-(cnt-1), key, curr_ptr+n+1))
                # res.append(key)
            # else:
                # res.append("idle")
            
            curr_ptr += 1

        # print(res)
        return curr_ptr