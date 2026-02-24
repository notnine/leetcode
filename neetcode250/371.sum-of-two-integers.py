#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF      # keeps numbers within 32 bits
        MAX_INT = 0x7FFFFFFF   # largest positive 32-bit integer

        # a is our partial sum, b is our carry
        # we & each op. with MASK to avoid overflow.

        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        
        if a > MAX_INT:
            return a - (2**32)
        return a

        
# @lc code=end

