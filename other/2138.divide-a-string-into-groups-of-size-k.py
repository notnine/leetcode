#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        curr = ''

        for c in s:
            if len(curr) == k:
                res.append(curr)
                curr = c
            else:
                curr += c
        
        if len(curr) == k:
            res.append(curr)
        else:
            curr += fill * (k - len(curr))
            res.append(curr)
        
        return res
# @lc code=end
