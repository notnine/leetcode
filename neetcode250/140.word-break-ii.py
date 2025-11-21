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
        memo = {}

        # i is the first index at s which is not in our partition yet
        def dfs(i: int) -> None:
            if i in memo:
                return memo[i]
            if i == n:
                return ['']
            
            res = []
            for j in range(i + 1, n + 1):
                # if s[i:j] is a word in word_set, dfs it
                if s[i:j] in word_set:
                    tails = dfs(j)
                    for tail in tails:
                        if tail != '':
                            res.append(s[i:j] + ' ' + tail)
                        else:
                            res.append(s[i:j])
            
            memo[i] = res
            return res
        
        return dfs(0)
# @lc code=end

