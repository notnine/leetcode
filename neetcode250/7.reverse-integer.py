#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        ub = 2**31 - 1 # lower bound, upper bound before overflowing
        res = 0
        is_negative = x < 0
        if is_negative:
            x *= -1

        while x != 0:

            # get last digit
            digit = x % 10

            # remove last digit
            x = x // 10

            # check if we will overflow, without overflowing
            if (res == ub // 10 and digit > ub % 10) or (res > ub // 10):
                return 0
            
            res *= 10
            res += digit
            
        return res if not is_negative else -res

# @lc code=end

