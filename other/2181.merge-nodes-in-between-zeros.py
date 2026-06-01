#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
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
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr_old = head.next
        temp = ListNode()
        curr_new = ListNode()
        temp.next = curr_new

        while curr_old:
            if curr_old.val != 0:
                curr_new.val += curr_old.val
            else:
                next_node = ListNode()
                if curr_old.next is not None:
                    curr_new.next = next_node
                    curr_new = next_node
            
            curr_old = curr_old.next

        return temp.next
# @lc code=end

