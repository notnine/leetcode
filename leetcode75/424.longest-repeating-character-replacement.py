#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        mf = 0 # count of most freq. char
        l, r = 0, 0
        res = 0

        # notice we do not have to udpate mf because we only update mf to keep track of res
        while r < len(s):
            freqs[s[r]] += 1
            mf = max(mf, freqs[s[r]])
            # while invalid, shrink till valid
            window_size = r - l + 1
            while window_size - mf > k:
                freqs[s[l]] -= 1
                l += 1
                window_size -= 1

            # at this point we have a valid window
            res = max(res, window_size)
            r += 1
    
        return res

# @lc code=end

