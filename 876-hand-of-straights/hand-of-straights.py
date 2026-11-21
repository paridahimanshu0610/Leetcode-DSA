import heapq

class Solution:
    def isNStraightHand(self, a: list[int], size: int) -> bool:
        n = len(a)
        if n % size != 0:
            return False

        temp = {}
        for e in a:
            temp[e] = 1 if e not in temp else temp[e]+1
        
        hp = list(temp.keys())
        heapq.heapify(hp)

        def decr(item):
            if item not in temp:
                return
                
            temp[item] -= 1
            if temp[item] == 0:
                del temp[item]

        for i in range(n//size):
            # Finding the current group's starting element from the heap.
            # We use heap to ensure that we always start from the lowest possible element
            min_e = heapq.heappop(hp)
            while min_e not in temp:
                min_e = heapq.heappop(hp)

            decr(min_e)
            if min_e in temp:
                heapq.heappush(hp, min_e)

            curr_item = min_e+1
            for _ in range(size-1):
                if curr_item not in temp:
                    return False
                else:
                    decr(curr_item)
                    curr_item += 1

        return True