#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    # return x's root
    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]] # path compression
            x = self.par[x]
        return x
    
    # union a & b (merging smaller to bigger)
    def union(self, a: int, b: int) -> None:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return
        
        # merge a into b
        if self.rank[pa] < self.rank[pb]:
            self.par[pa] = pb
        
        # merge b into a
        elif self.rank[pa] > self.rank[pb]:
            self.par[pb] = pa
        
        # merge b into a, increment a's rank
        else:
            self.par[pb] = pa
            self.rank[pa] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)        
        uf = UnionFind(n) # uf holds indices
        index_to_name = {i: account[0] for i, account in enumerate(accounts)}
        email_to_index = {}

        # union accounts with common emails
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_index:
                    uf.union(i, email_to_index[email])
                email_to_index[email] = i

        # group emails by root index
        root_to_emails = defaultdict(set)
        for email, i in email_to_index.items():
            root = uf.find(i)
            root_to_emails[root].add(email)

        # build return list
        res = []
        for root, emails in root_to_emails.items():
            curr = [index_to_name[root]]
            curr.extend(sorted(emails))
            res.append(curr.copy())
        return res

# @lc code=end

