from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = deque(), deque()
        n = len(senate)

        for i in range(len(senate)):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            ri, di = r.popleft(), d.popleft()
            if ri < di:
                r.append(ri+n)
            else:
                d.append(di+n)

        return "Radiant" if r else "Dire"