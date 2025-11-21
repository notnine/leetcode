#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)
        res = []

        # i is the first index at s which is not in our partition yet
        def backtrack(i: int, partition: List[str]) -> None:
            if i == n:
                res.append(" ".join(partition))
                return
            
            for j in range(i + 1, n + 1):
                # if s[i:j] is a word in word_set, backtrack it
                if s[i:j] in word_set:
                    partition.append(s[i:j])
                    backtrack(j, partition)
                    partition.pop()
        
        backtrack(0, [])
        return res
# @lc code=end

