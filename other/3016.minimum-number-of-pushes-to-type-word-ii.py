#
# @lc app=leetcode id=3016 lang=python3
#
# [3016] Minimum Number of Pushes to Type Word II
#

# @lc code=start
from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        # from the num of unique chars, how many can we fit into 8 buttons

        # get all the unique characters, get all their frequencies
        # sort frequencies in descending order. We want to map the more frequent chars to less pushes
        # for each button (freq), take the num of pushes we need and sum it all up

        char_to_freq = Counter(word)
        freqs = sorted(char_to_freq.values(), reverse=True)
        res = 0

        for i, f in enumerate(freqs):
            pushes = ((i // 8) + 1) * f
            res += pushes
        
        return res

 
# @lc code=end

