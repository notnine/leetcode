#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import deque, defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # adj list maps variable to list of tuples (variable, weight)
        adj = defaultdict(list)
        for i, equation in enumerate(equations):
            a, b = equation[0], equation[1]
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        
        # given src & dst, return value if exists, -1 o|w
        def bfs(src: str, dst: str) -> int:
            if src not in adj or dst not in adj:
                return -1
            q = deque()
            visitted = set()
            q.append((src, 1))
            visitted.add(src)
            while q:
                v, w = q.pop()
                if v == dst:
                    return w
                for nei_v, nei_w in adj[v]:
                    if nei_v not in visitted:
                        visitted.add(nei_v)
                        q.append((nei_v, nei_w * w))
            return -1
        
        return [bfs(src, dst) for src, dst in queries]
# @lc code=end

