#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#

# @lc code=start
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        # build adj. list
        neis = defaultdict(list)
        for a, b in prerequisites:
            neis[b].append(a)

        prereqs = defaultdict(set) # basically memoize each query

        # put all the prereqs of c into prereqs[c]
        def dfs(c: int) -> set:
            if c in prereqs:  # already computed
                return prereqs[c]
            for nei in neis[c]:
                prereqs[c].add(nei)
                prereqs[c] |= dfs(nei)  # union with neighbor’s prereqs
            return prereqs[c]

        # build return list
        res = []
        for u, v in queries:
            if v in prereqs:
                res.append(u in prereqs[v])
            else:
                dfs(v)
                res.append(u in prereqs[v])

        return res    
# @lc code=end

