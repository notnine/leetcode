#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        res = []
        carry = 0

        while i >= 0 or j >= 0 or carry > 0:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            res.append(str(total % 2)) # append right most bit
            carry = total // 2 # append left most bit

        return ''.join(res[::-1])
# @lc code=end

