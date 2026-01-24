#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        # prereq node is not None
        def bfs(node: TreeNode, path: str):
            path += str(node.val) + '->'
            if not node.left and not node.right:
                path = path[:len(path) - 2]
                res.append(path)
                return
            if node.left:
                bfs(node.left, path)
            if node.right:
                bfs(node.right, path)
        
        if not root:
            return []

        bfs(root, '')
        return res
# @lc code=end

