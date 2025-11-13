#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = [] # we use list instead of string because we need seperators b/w values. for e.g what if val is 14

        # traverse tree pre-order (root, left, right) & put val into res
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal res
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(',') # get back our res array
        n = len(res)
        i = 0 # keeps track of the index our dfs is at
        
        # pre-req: i is in bounds
        # recursively build tree, returning the node at that index
        def dfs() -> Optional[TreeNode]:
            nonlocal res, n, i
            if res[i] == 'N':
                i += 1
                return None
            else:
                curr = TreeNode(val=int(res[i]))
                i += 1
                curr.left = dfs() # attach left subtree
                curr.right = dfs() # attach right subtree
                return curr

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

