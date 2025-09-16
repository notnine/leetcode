#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # 1. find the a piece of the island
        # 2. traverse the island (dfs)
        # 3. while traversing:
            # for each unvisited land, count water borders

        visited = set() # represents visited lands
        res = 0 # represents the island perimeter
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # (i,j) represents (row, col) unvisited land coord in grid
        def dfs(i: int, j: int) -> None:
            nonlocal res
            visited.add((i, j))
            # count the num of sides (i,j) touches water
            for dir_i, dir_j in directions:
                # if neighbouring pos is out of position or water
                new_i, new_j = i + dir_i, j + dir_j
                if not (0 <= new_i < len(grid)) or not (0 <= new_j < len(grid[0])) or grid[new_i][new_j] == 0:
                    res += 1
            # traverse unvisited lands
            for dir_i, dir_j in directions:
                new_i, new_j = i + dir_i, j + dir_j
                if (0 <= new_i < len(grid)) and (0 <= new_j < len(grid[0])) and grid[new_i][new_j] == 1 and (new_i, new_j) not in visited:
                    dfs(new_i, new_j)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: # found land
                    dfs(i, j)
                    return res   
# @lc code=end

