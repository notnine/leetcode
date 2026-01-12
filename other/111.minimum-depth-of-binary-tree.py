#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        curr_lvl = deque([root])
        depth = 0

        while curr_lvl:
            depth += 1
            next_lvl = deque([])
            for _ in range(len(curr_lvl)):
                curr_node = curr_lvl.popleft()
                if not curr_node.left and not curr_node.right:
                    return depth
                if curr_node.left:
                    next_lvl.append(curr_node.left)
                if curr_node.right:
                    next_lvl.append(curr_node.right)
            curr_lvl = next_lvl
            next_lvl = deque([])
        
        return depth
        
            



# @lc code=end

