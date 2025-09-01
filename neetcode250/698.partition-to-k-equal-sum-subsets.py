#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        curr = [0] * k # represents the sums of our k subsets
        nums.sort(reverse=True) # to prevent repeated work thru pruning
        target = sum(nums) // k

        # return true if we can create k equal subset sums, where i is our curr index
        def backtrack(i: int) -> bool:
            print(curr)
            print()
            if i == len(nums):
                return all(curr[j] == target for j in range(k))
            
            # try putting nums[i] in all subsets
            for j in range(k):
                if curr[j] + nums[i] <= target:
                    curr[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    # else try another spot
                    curr[j] -= nums[i]

                # if the subset was 0, the other subsets are 0 too, and that's repeated work so just skip
                if curr[j] == 0:
                    break

            return False
        
        return backtrack(0)
# @lc code=end

