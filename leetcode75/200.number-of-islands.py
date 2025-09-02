#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_islands = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # visit entire island
        # actually this is dfs
        def bfs(i: int, j: int) -> None:
            visited.add((i, j))
            for dir_i, dir_j in directions:
                new_i, new_j = dir_i + i, dir_j + j
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == '1' and (new_i, new_j) not in visited:
                    bfs(new_i, new_j)

            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    num_islands += 1
                    bfs(i, j)

        return num_islands
        
# @lc code=end


        
# @lc code=end

