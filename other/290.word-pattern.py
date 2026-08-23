#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(' ')
        words_to_index = defaultdict(list)

        for i, word in enumerate(words):
            words_to_index[word].append(i)
        
        letters_to_index = defaultdict(list)

        for i, letter in enumerate(pattern):
            letters_to_index[letter].append(i)

        return list(words_to_index.values()) == list(letters_to_index.values())
# @lc code=end

