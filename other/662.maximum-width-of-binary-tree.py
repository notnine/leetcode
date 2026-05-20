#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
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
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        nodes = deque([(root, 0)])
        max_width = 0

        while nodes:
            n = len(nodes)
            curr_width = 1
            left_most_i, right_most_i = None, None

            for _ in range(n):
                node, i = nodes.popleft()
                if node.left:
                    if left_most_i is None:
                        left_most_i = 2 * i
                    right_most_i = 2 * i
                    nodes.append((node.left, 2 * i))
                if node.right:
                    if left_most_i is None:
                        left_most_i = 2 * i + 1
                    right_most_i = 2 * i + 1
                    nodes.append((node.right, 2 * i + 1))

            if left_most_i is not None and right_most_i is not None:
                curr_width = right_most_i - left_most_i + 1
            max_width = max(max_width, curr_width)
        
        return max_width

# @lc code=end

