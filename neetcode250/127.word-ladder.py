#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        # return True if word1 and word2 differ by 1 letter. Pre-req word1 != word2
        def is_neighbor(word1: str, word2: str) -> bool:
            diffs = 0
            n = len(word1)
            for i in range(n):
                if word1[i] != word2[i]:
                    diffs += 1
                if diffs > 1:
                    return False
            return True
        
        # create adj list
        neighbors = defaultdict(list)
        wordList.append(beginWord)
        n = len(wordList)
        for i in range(n):
            for j in range(i + 1, n):
                word1, word2 = wordList[i], wordList[j]
                if is_neighbor(word1, word2):
                    neighbors[word1].append(word2)
                    neighbors[word2].append(word1)

        # run bfs, try to reach endWord asap
        q = deque([beginWord])
        res = 1
        visited = set()
        visited.add(beginWord)

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for neighbor in neighbors[word]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            res += 1
        
        return 0
# @lc code=end

