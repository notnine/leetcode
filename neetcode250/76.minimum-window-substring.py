#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        t_ctr = Counter(t)
        
        # return True if w_ctr is a valid window substring ctr of t_ctr
        def valid_substring(w_ctr: Counter) -> bool:
            for k, v in t_ctr.items():
                if w_ctr[k] < v:
                    return False
            return True

        res = ''
        l = 0
        w_ctr = Counter()
        
        for r, c in enumerate(s):
            w_ctr[c] += 1

            while valid_substring(w_ctr) and l <= r:
                if res== '':
                    res = s[l:r+1]
                else:
                    res = res if len(res) < r - l + 1 else s[l:r+1]
                w_ctr[s[l]] -= 1
                if w_ctr[s[l]] == 0: del w_ctr[s[l]]
                l += 1

        return res
        
# @lc code=end

