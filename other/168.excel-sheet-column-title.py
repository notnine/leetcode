#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        res = ''

        while columnNumber > 0:
            columnNumber -= 1
            curr = columnNumber % 26
            res = letters[curr] + res
            columnNumber //= 26
        
        return res
# @lc code=end

