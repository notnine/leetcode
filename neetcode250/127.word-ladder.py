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

        wordSet = set(wordList)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        # create adj list
        neighbors = defaultdict(list)
        wordList.append(beginWord)
        n = len(wordList)
        for word in wordList:
            # find all neighbors of word
            for i, c in enumerate(word):
                for letter in letters:
                    if letter == c:
                        continue
                    word_to_check = word[:i] + letter + word[i+1:]
                    if word_to_check in wordSet:
                        neighbors[word].append(word_to_check)
                        neighbors[word_to_check].append(word)


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

