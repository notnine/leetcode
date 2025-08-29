#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
                memo = {}

        # skip is true if node is skipped
        def dfs(node: Optional[TreeNode], skip: bool) -> int:
            if not node: return 0
            if (node, skip) in memo: return memo[(node, skip)]

            if skip:
                skip_left = dfs(node.left, True)
                skip_right = dfs(node.right, True)
                use_left = dfs(node.left, False)
                use_right = dfs(node.right, False)
                memo[(node, skip)] = max(skip_left, use_left) + max(use_right, skip_right)
            else:
                memo[(node, skip)] = node.val + dfs(node.left, True) + dfs(node.right, True)
            
            return memo[(node, skip)]
             
        
        return max(dfs(root, True), dfs(root, False))
# @lc code=end

