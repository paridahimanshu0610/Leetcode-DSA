from heapq import *

class Solution:
    def identify_tasks(self, start_index, curr_time, lt):
        for i in range(start_index, len(lt)):
            task_enqueue_time, task_processing_time, _ = lt[i] 
            if task_enqueue_time > curr_time:
                return i

        return len(lt)

    def getOrder(self, a: List[List[int]]) -> List[int]:
        lt = [(temp[0], temp[1], i) for i, temp in enumerate(a)] # labeled tasks
        lt.sort()

        curr_time = lt[0][0] #Enqueue time of the first task
        curr_tasks = []
        heapify(curr_tasks)
        completed_tasks = []
        curr_index = 0

        while len(completed_tasks) < len(a) and curr_index < len(lt):
            while curr_index < len(lt) and curr_time >= lt[curr_index][0]:
                heappush(curr_tasks, [lt[curr_index][1], lt[curr_index][2]])
                curr_index += 1

            if len(curr_tasks)==0:
                curr_time = lt[curr_index][0]
            else:
                process_time, idx = heappop(curr_tasks)
                completed_tasks.append(idx)
                curr_time += process_time 

        while len(completed_tasks) < len(a):
            process_time, idx = heappop(curr_tasks)
            completed_tasks.append(idx)
                        
        return completed_tasks 