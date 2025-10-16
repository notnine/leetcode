#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = 0
        res = []
        dq = deque() # stores indices, in the order of biggest & oldest -> smallest & newest

        while r < len(nums):
            # while nums[r] is larger than the tail of the queue, pop tail off
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()

            # append r to dq
            dq.append(r)

            # if head index is out of window, popleft
            if dq and dq[0] < (r - k + 1):
                dq.popleft()

            # append nums[dq[0]] to res
            if (r - k + 1) >= 0:
                res.append(nums[dq[0]])

            r += 1

        return res
            
            

# @lc code=end

