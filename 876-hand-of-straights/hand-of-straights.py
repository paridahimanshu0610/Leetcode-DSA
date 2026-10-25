import heapq 

class Solution:
    def isNStraightHand(self, a: list[int], size: int) -> bool:
        n = len(a)
        if n%size != 0:
            return False

        k = n//size

        temp = {}
        for e in a:
            temp[e] = 1 if e not in temp else temp[e]+1
            
        hp = list(temp.keys())
        heapq.heapify(hp)

        def decr(key):
            temp[key] -= 1
            if temp[key] == 0:
                del temp[key]

        for i in range(k):
            min_e = heapq.heappop(hp)
            while min_e not in temp:
                min_e = heapq.heappop(hp)
            decr(min_e)
            if min_e in temp:
                heapq.heappush(hp, min_e)

            next_e = min_e+1
            for j in range(size-1):
                if next_e not in temp:
                    return False
                else:
                    decr(next_e)
                    next_e += 1

        return True 