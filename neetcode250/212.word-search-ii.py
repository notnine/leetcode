#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self, c: str = '', is_word: bool = False):
        self.c = c
        self.is_word = is_word
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c, False)
            node = node.children[c]
        node.is_word = True                

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(node: TrieNode, r: int, c: int, visited: Set[tuple], path: str):
            nonlocal res
            if node.is_word:
                res.append(path)
                node.is_word = False   # avoid duplicates, i.e re-adding same word
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and board[nr][nc] in node.children:
                    ch = board[nr][nc]
                    visited.add((nr, nc))
                    dfs(node.children[ch], nr, nc, visited, path + ch)
                    visited.remove((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                ch = board[r][c]
                if ch in trie.root.children:
                    visited = {(r, c)}
                    dfs(trie.root.children[ch], r, c, visited, ch)
                if len(res) == len(words):
                    return res
        
        return res


# @lc code=end

