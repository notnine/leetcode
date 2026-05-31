#
# @lc app=leetcode id=2109 lang=python3
#
# [2109] Adding Spaces to a String
#

# @lc code=start
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        i = 0

        for space in spaces:
            res.append(s[i:space])
            res.append(' ')
            i = space
        
        # append the rest
        res.append(s[i:])

        return ''.join(res)

# @lc code=end

