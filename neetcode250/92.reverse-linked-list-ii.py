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

        dummy = ListNode(0, head)
        prev = dummy

        # point prev to left - 1
        for _ in range(1, left):
            prev = prev.next
        
        left_minus_one = prev
        sublist_tail = left_minus_one.next

        # reverse our sublist
        sublist_prev = None
        sublist_curr = sublist_tail
        # 1 -> 2 -> 3 -> 4 -> 5 ; reversing 2 to 4
        for _ in range(left, right + 1):
            temp = sublist_curr.next
            sublist_curr.next = sublist_prev
            sublist_prev, sublist_curr = sublist_curr, temp
        

        # attach left_minus_one to sublist head
        left_minus_one.next = sublist_prev
        # attach sublist tail to right + 1
        sublist_tail.next = sublist_curr

        return dummy.next


# @lc code=end

