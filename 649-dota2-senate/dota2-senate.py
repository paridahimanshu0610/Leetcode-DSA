from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = deque(), deque()
        r_set, d_set = set(), set()

        for i in range(len(senate)):
            if senate[i] == "R":
                r.append(i)
                r_set.add(i)
            else:
                d.append(i)
                d_set.add(i)

        while True:
            for i in range(len(senate)):
                if (senate[i]=="R") and (i in r_set):
                    if len(d) == 0:
                        return "Radiant"
                    else:
                        d_set.remove(d.popleft())
                        r.append(r.popleft())
                elif (senate[i]=="D") and (i in d_set):
                    if len(r) == 0:
                        return "Dire"
                    else:
                        r_set.remove(r.popleft())
                        d.append(d.popleft())

        return "Radiant"