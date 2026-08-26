#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = int(a, 2) + int(b, 2)
        return bin(res)[2:]     
# @lc code=end

