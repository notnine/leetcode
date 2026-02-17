#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0]) if mat else 0

        # not possible
        if n*m != r*c:
            return mat

        res = [[0 for _ in range(c)] for _ in range(r)]
        curr_r, curr_c = 0, 0 # pointers to original mat
        for i in range(r):
            for j in range(c):
                res[i][j] = mat[curr_r][curr_c]
                curr_c += 1
                if curr_c >= m:
                    curr_c = 0
                    curr_r += 1
        
        return res
# @lc code=end

