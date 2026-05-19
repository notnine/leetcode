#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#

# @lc code=start
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        memo = {} # memo[node] = [freqs for all 26 colors]
        visiting = set()

        # init adj graph

        # return [freqs for all 26 colors] for node
        def dfs(node):
            if node in memo:
                return memo[node]
            if node in visiting:
                return None
            visiting.add(node)
            # init [0 for eveyr color], i.e counts freq for this node
            # call dfs for every outgoing edge, for every color, take the highest freq path, put it in counts freq
            # add node's color to count freq
            # visiting.remove(node)
            # return memo[node]
            


        # call dfs on every node, iterate thru memo to find the largest frequency
        # for node in nodes:
            # dfs(node)
            # visiting = set()
# @lc code=end

