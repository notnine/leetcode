#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        memo = {} # longest increasing path from each position

        # given current pos & visited set, return longest increasing path in matrix
        def dfs(i: int, j: int, visited: set) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 0
            for direction in directions:
                new_i, new_j = i + direction[0], j + direction[1]
                if 0 <= new_i < ROWS and 0 <= new_j < COLS and (new_i, new_j) not in visited and matrix[new_i][new_j] > matrix[i][j]:
                    visited.add((new_i, new_j))
                    res = max(res, 1 + dfs(new_i, new_j, visited))
                    visited.remove((new_i, new_j))
            
            memo[(i, j)] = res
            return res
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                visited = set()
                res = max(res, 1 + dfs(i, j, visited))
        return res
# @lc code=end

