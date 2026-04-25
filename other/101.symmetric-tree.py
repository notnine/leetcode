#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        def same_mirror(left, right):
            if not left and not right:
                return True
            
            if (not left and right) or (left and not right) or (left.val != right.val):
                return False
            
            return same_mirror(left.left, right.right) and same_mirror(left.right, right.left)

        return same_mirror(root.left, root.right)  
# @lc code=end

