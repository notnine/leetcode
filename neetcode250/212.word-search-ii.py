#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # return True if word is in board (word search 1). curr_pos is the last visited pos, visited is our word so far (positions)
        def dfs(word: str, visited: set, curr_pos: tuple) -> bool:
            if word is None or word == '':
                return True

            for direction in directions:
                new_i, new_j = direction[0] + curr_pos[0], direction[1] + curr_pos[1]
                if 0 <= new_i < ROWS and 0 <= new_j < COLS and board[new_i][new_j] == word[0] and (new_i, new_j) not in visited:
                    visited.add((new_i, new_j))
                    if dfs(word[1:], visited, (new_i, new_j)): # if this route is possible return True early
                        return True
                    visited.remove((new_i, new_j))
            return False

        res = []
        for word in words:
            found_word = False
            for i in range(ROWS):
                for j in range(COLS):
                    if board[i][j] == word[0]:
                        if dfs(word[1:], {(i, j)}, (i, j)):
                            res.append(word)
                            found_word = True
                    if found_word:
                        break
                if found_word:
                    break

        return res                            
                            

# @lc code=end

