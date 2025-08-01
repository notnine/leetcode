#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]

    # return root of x's tree
    def find(self, x: int) -> int:
        # path compression: point parent of x to its tree's root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # merge trees x and y
    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        # skipping ranks for now
        if root_x != root_y: self.parent[root_y] = root_x

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # simplest sol. would be adj. graph + dfs/bfs, but union find is used for practice.
        union_find = UnionFind(n)

        for u, v in edges:
            union_find.union(u, v)
        
        return union_find.find(source) == union_find.find(destination)



# @lc code=end

