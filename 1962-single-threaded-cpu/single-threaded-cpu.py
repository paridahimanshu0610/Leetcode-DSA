import heapq as hq
class Solution:
    def getOrder(self, a: List[List[int]]) -> List[int]:
        for i in range(len(a)):
            a[i] = [i] + a[i]
        a.sort(key = lambda x: (x[1], x[2]))
        task_heap = []
        hq.heapify(task_heap)

        curr_time = a[0][1]
        res = []
        curr_task = 0

        while curr_task < len(a):
            # Pushing all currently available tasks onto the heap
            while curr_task < len(a) and a[curr_task][1] <= curr_time:
                hq.heappush(task_heap, [a[curr_task][2], a[curr_task][0]])
                curr_task += 1
            
            if len(task_heap) > 0:
                process_time, idx = hq.heappop(task_heap)
                res.append(idx)
                curr_time += process_time
            else:
                if curr_task < len(a):
                    curr_time = a[curr_task][1]

        while len(task_heap) > 0:
            _, idx = hq.heappop(task_heap)
            res.append(idx)            
        
        return res