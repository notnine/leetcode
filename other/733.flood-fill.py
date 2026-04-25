#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS, COLS = len(image), len(image[0])
        ori_color = image[sr][sc]

        curr = [(sr, sc)] if image[sr][sc] != color else []
        image[sr][sc] = color

        while curr:
            r, c = curr.pop()
            for d_r, d_c in directions:
                n_r, n_c = r + d_r, c + d_c
                if 0 <= n_r < ROWS and 0 <= n_c < COLS and image[n_r][n_c] == ori_color:
                    curr.append((n_r, n_c))
                    image[n_r][n_c] = color
        
        return image
# @lc code=end

