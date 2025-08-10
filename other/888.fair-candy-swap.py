#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#

# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)
        bob_set = set(bobSizes)

        for box in aliceSizes:
            if (bob_sum + 2 * box - alice_sum) // 2 in bob_set:
                return [box, (bob_sum + 2 * box - alice_sum) // 2]
        
# @lc code=end

