#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        curr_row = [1,1]
        curr_i = 1

        while curr_i != rowIndex:
            i, j = 0, 1
            new_row = [1]
            while j < len(curr_row):
                new_row.append(curr_row[i] + curr_row[j])
                i, j = i + 1, j + 1
            new_row.append(1)
            curr_row = new_row
            curr_i += 1

        return curr_row


# @lc code=end

