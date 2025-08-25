#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # edge case, if left == 1, then detached left - 1 is None
        
        # detach left - 1 & right + 1
        
        prev, curr = None, head
        while curr:


        # run reverseLinkedList on left as head

        # re-attach left - 1 to head of reversed, and tail of reversed to right + 1
# @lc code=end

