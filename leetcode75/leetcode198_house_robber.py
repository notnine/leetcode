class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        # recursion relation: we are at house i. either we rob house i, or we rob house i - 1
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
             dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            
        return dp[len(nums) - 1]