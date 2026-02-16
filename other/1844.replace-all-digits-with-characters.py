#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        s_arr = list(s)
        res = []

        for i, c in enumerate(s):
            if i % 2 != 0:
                new_c = chr(ord(res[-1]) + int(c))
                res.append(new_c)
            else:
                res.append(c)

        return ''.join(res)# @lc code=end

