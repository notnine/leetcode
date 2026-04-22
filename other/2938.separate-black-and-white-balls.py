#
# @lc app=leetcode id=2938 lang=python3
#
# [2938] Separate Black and White Balls
#

# @lc code=start
class Solution:
    def minimumSteps(self, s: str) -> int:
        # 1: black, 0: white
        # left white, right black

        # 100

        # black: [0]
        # white: [1,2]

        # n_black = 1
        # n_white = 2
        # n = 3

        # want black to be from indices n - n_black to n-1 (last index). here it's 2 to 2
        # want white to be from 0 to n_white - 1

        # if black and white arrays are sorted already,
        # then we can just calculate the differences for each index

        n = len(s)
        n_black, n_white = 0, 0
        black, white = [], []
        for i, c in enumerate(s):
            if c == '1':
                n_black += 1
                black.append(i)
            else:
                n_white += 1
                white.append(i)

        # so we want black to be from indices:
        black_first_i = n - n_black
        # want white to be from indices:
        white_first_i = 0

        total_diff = 0

        # we calc the differences in ideal indices
        for i, b in enumerate(black):
            total_diff += abs(b - (black_first_i + i))
        for i, w in enumerate(white):
            total_diff += abs(w - (white_first_i + i))

        # and we divide this total by 2
        return total_diff // 2
# @lc code=end

