#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        letter_to_index = {}
        max_range = 0
        curr = None

        for i, c in enumerate(s):
            if c not in letter_to_index:
                letter_to_index[c] = [i]
            
            else:
                if len(letter_to_index[c]) == 1:
                    letter_to_index[c].append(i)
                else:
                    letter_to_index[c][1] = i

                diff = letter_to_index[c][1] - letter_to_index[c][0]
                if diff > max_range:
                    max_range = diff
                    curr = letter_to_index[c]
        
        if not curr:
            return -1
        
        return max_range - 1
# @lc code=end

