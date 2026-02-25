#
# @lc app=leetcode id=1974 lang=python3
#
# [1974] Minimum Time to Type Word Using Special Typewriter
#

# @lc code=start
class Solution:
    def minTimeToType(self, word: str) -> int:
        res = len(word)
        word = 'a' + word

        for i in range(len(word) - 1):
            diff = abs(ord(word[i+1]) - ord(word[i]))
            clockwise = diff
            anti_clockwise = 26 - diff
            res += min(clockwise, anti_clockwise)

        return res
# @lc code=end

