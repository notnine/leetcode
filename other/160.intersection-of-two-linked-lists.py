#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: return None

        ptr_a = headA
        ptr_b = headB

        while ptr_a is not ptr_b:
            ptr_a = ptr_a.next if ptr_a else headB
            ptr_b = ptr_b.next if ptr_b else headA
        return ptr_a
            
# @lc code=end

