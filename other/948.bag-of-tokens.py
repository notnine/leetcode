#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        l, r = 0, n - 1
        score = 0
        best_score = 0

        # while we cna do smth, and indices are still valid
        while l <= r:
            # if we can't play token[l] and we can't gain power
            if power < tokens[l] and score == 0:
                return best_score
            # if we can't play token[l], gain power
            elif power < tokens[l] and score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                score += 1
                power -= tokens[l]
                l += 1
            best_score = max(best_score, score)


        return best_score
# @lc code=end

