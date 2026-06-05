#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(val=-1, next=head)
        prev, curr = dummy, head

        while curr:
            while curr and curr.val == val:
                curr = curr.next
            prev.next = curr
            prev = curr
            curr = prev.next if prev else None
            
        return dummy.next
# @lc code=end

