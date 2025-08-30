#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # list containing num_passengers update. for e.g., -3 at km 7 for dropping 3 passengers off at km 7 or 3 at km 7 for picking up 3 at km 7
        states = [] # (dist, +/- num_passengers)

        for num_passengers, f, t in trips:
            states.append((f, num_passengers))
            states.append((t, -num_passengers))

        states.sort() # sort states in ascending order of dist (1) and num_passengers (2). we drop off passengers first
        curr = 0 # number of passengers that we are currently holding

        for d, num_passengers in states:
            curr += num_passengers
            if curr > capacity:
                return False

        return True


# @lc code=end

