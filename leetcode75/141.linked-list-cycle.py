#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        slow = head
        fast = head.next

        while slow and fast and fast.next:
            if slow is fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        
        return False
# @lc code=end

