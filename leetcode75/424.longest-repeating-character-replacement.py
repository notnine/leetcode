#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, n = 0, len(s)
        mf = 0
        res = 0
        window = defaultdict(int) # counter for current window

        for r in range(n):
            # expand window
            window[s[r]] += 1

            # update most frequent char f
            mf = max(mf, window[s[r]])

            # while window invalid, shrink til valid
            while (r - l + 1) - mf > k: # invalid
                window[s[l]] -= 1
                l += 1

            # update res
            res = max(res, r - l + 1)

        return res

# @lc code=end

