#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#
from collections import deque

# @lc code=start
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # 1. rewrite tasks to be of tuples (start_time, process_time, index)
        # 2. sort tasks by start_time
        # 3. maintain heap of available tasks
            # min heap sorted by 1. process_time 2. index
        # 4. maintain "time" starting at 0. simulate CPU process by looping over heap.

        # Step 1
        for index, task in enumerate(tasks):
            tasks[index] = (task[0], task[1], index)

        # Step 2
        tasks = sorted(tasks)
        tasks = deque(tasks)
        
        # Step 3
        t = 0
        res = []
        heap = []

        while tasks or heap:
            # while tasks is nonempty, add all of the avialable tasks into our heap
            while tasks and tasks[0][0] <= t:
                avialable_task = tasks.popleft()
                heapq.heappush(heap, (avialable_task[1], avialable_task[2]))
            # process the next available task, jump to the time when this task is finished
            if heap:
                process_time, index = heapq.heappop(heap)
                res.append(index)
                t += process_time
            else:
                if not tasks:
                    return res
                else:
                    next_task = tasks.popleft()
                    t = next_task[0]
                    heapq.heappush(heap, (next_task[1], next_task[2]))

        return res
# @lc code=end