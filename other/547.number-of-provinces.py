#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]

    # return x's root
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # build union find instance
        n = len(isConnected)
        union_find = UnionFind(n)
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union_find.union(i, j)

        # count distinct number of roots
        num_roots = 0
        visited = set()
        for i in range(n):
            root = union_find.find(i)
            if root not in visited:
                num_roots += 1
                visited.add(root)
        
        return num_roots

# @lc code=end

