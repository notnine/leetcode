#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    # return root of x's tree & compress path
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # merge x's tree and y's tree
    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        rank_x, rank_y = self.rank[root_x], self.rank[root_y]
        if root_x != root_y:
            # merge smaller tree to the bigger one
            if rank_x < rank_y:
                self.parent[root_x] = root_y
            elif rank_x > rank_y:
                self.parent[root_y] = root_x
            else: # rank will increase since we are merging trees of the same size
                self.parent[root_x] = root_y
                self.rank[root_y] += 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # we will just 0 index the indices, and remember

        # build our union find instance
        n = 0
        for x, y in edges:
            x, y = x - 1, y - 1
            n = max(n, x, y)
        union_find = UnionFind(n + 1)

        # build union find, but if we find that x, y share the same root, return
        for x, y in edges:
            x, y = x - 1, y - 1
            root_x, root_y = union_find.find(x), union_find.find(y) # O(E \alpha{n}) time
            if root_x == root_y:
                return [x+1, y+1]
            else:
                union_find.union(x, y)
# @lc code=end

