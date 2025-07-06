#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        curr_stus = len(students)
        stus = deque(students)
        sands = deque(sandwiches)

        while stus:
            if curr_stus == 0:
                return len(stus)

            if stus[0] == sands[0]:
                stus.popleft()
                sands.popleft()
                curr_stus = len(stus)
            else:
                curr_stus -= 1
                stu = stus.popleft()
                stus.append(stu)

        return 0


# @lc code=end

