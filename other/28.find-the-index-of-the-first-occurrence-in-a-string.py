#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, n = 0, len(haystack)
        k = len(needle)

        while i <= n - k:
            if haystack[i:i+k] == needle:
                return i
            i += 1
        
        return -1
# @lc code=end

