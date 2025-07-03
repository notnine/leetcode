#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        curr_lvl = deque([root])
        left_to_right = False
        res = [[root.val]]

        while curr_lvl:
            next_lvl = []
            while curr_lvl:
                curr_node = curr_lvl.popleft()
                if curr_node.left: next_lvl.append(curr_node.left)
                if curr_node.right: next_lvl.append(curr_node.right)
            if left_to_right:
                if next_lvl: res.append([n.val for n in next_lvl])
                left_to_right = False
            else:
                if next_lvl: res.append([n.val for n in next_lvl][::-1])
                left_to_right = True
            curr_lvl = deque(next_lvl)

        return res
                





# @lc code=end

