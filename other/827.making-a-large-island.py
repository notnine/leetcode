#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # greedy: connect 2 of the biggest islands that are seperated by 1 water
        # basically, find the 2 biggest islands seperated by 1 water, return their sizes + 1

        # find all islands and their sizes

        # for each island, find their biggest neighbor seperated by 1 water -> hard part
        # keep track of the largest pair so far

        # return the result

        # ds needed
        # note islands are represented by 1 of their land points
        # hashmap all the land points -> their island
        # hashmap of all the islands -> area
        # biggest pair so far

        land_to_island = {} # maps (r, c) to starting (r, c)
        island_to_area = {} # starting (r, c) to land (int)
        
        # 0. build land_to_island, island_to_area
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        n = len(grid)
        def dfs(r: int, c: int, start: tuple(i, j)) -> None:
            island_to_area[start] += 1

            for d_r, d_c in directions:
                new_r, new_c = d_r + r, d_c + c
                if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    land_to_island[(new_r, new_c)] = start
                    dfs(new_r, new_c, start)

        for r in range(n):
            for c in range(n):
                if (r, c) not in visited and grid[r][c] == 1:
                    visited.add((r, c))
                    land_to_island[(r, c)] = (r, c)
                    island_to_area[(r, c)] = 0
                    dfs(r, c, (r, c))
        
        # 1. for each island, find their biggest neighbor seperated by 1 water, keep track of biggest pair so far
        # 1. instead of finding the largest neighbor of each island, traverse thru all water points, and find all the islands it is connected to. We aren't constrainted to 2 islands, 1 water can connect 4 islands. keep track of the best water
        best_water = 0
        for r in range(n):
            for c in range(n):
                curr_water = 0 # the island areas this water is connected too
                islands_visited = set() # islands we have traversed in this water, because 1 island might "circle" a water
                if grid[r][c] == 0:
                    for d_r, d_c in directions:
                        neighbor_r, neighbor_c = r + d_r, c + d_c
                        if 0 <= neighbor_r < n and 0 <= neighbor_c < n and grid[neighbor_r][neighbor_c] == 1:
                            island_start = land_to_island[(neighbor_r, neighbor_c)]
                            if island_start not in islands_visited:
                                islands_visited.add(island_start)
                                island_size = island_to_area[(island_start)]
                                curr_water += island_size
                best_water = max(best_water, curr_water)
        
        # if there's no water, then there's only 1 island, or no land
        if best_water == 0:
            if (0,0) in island_to_area:
                return island_to_area[(0,0)]
            else:
                0

        return best_water + 1
# @lc code=end

