#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal res
            # if neighbor not land, res += 1, else queue them to dfs
            for d_i, d_j in dirs:
                new_r, new_c = d_i + r, d_j + c
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    dfs(new_r, new_c) 
                else:
                    if not (0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 1):
                        res += 1

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c))
                    dfs(r, c)
                    return res
        
        return 0
# @lc code=end

