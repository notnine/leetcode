#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # mark all negative numbers as 0
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        # solution space is only 1 .. n + 1
        # for num that could be a sol, mark num - 1 as negative. if it was 0, change it to -(n+1)
        for num in nums:
            num = abs(num) # in case it was previously changed
            
            # if num in sol space
            if 1 <= num <= n:
                if nums[num - 1] == 0:
                    nums[num - 1] = -(n+1)

                # if not alr marked negative
                elif not (nums[num - 1] < 0):
                    nums[num - 1] *= -1
                
                # if alr marked negative do nothing. code for explicit logic
                else:
                    continue


        # iterate thru solution space, return earliest non-existent num
        for i in range(1, n+1):
            if not (nums[i - 1] < 0):
                return i
        
        return n + 1
        
# @lc code=end

