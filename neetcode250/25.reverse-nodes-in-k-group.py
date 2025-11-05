#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # return k^th from and including node (including node, and kth = n nodes)
        def get_kth(node: ListNode):
            for _ in range(k-1):
                if not node:
                    return None
                node = node.next
                
            return node

        if k <= 1 or not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy
        kth_node = get_kth(head)
        group_next = kth_node.next if kth_node else None

        while kth_node:
            # reverse current group
            prev = ListNode(0)
            curr  = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # attach reversed current group to prev group and next group
            new_tail = group_prev.next # group's previous head is now the tail
            group_prev.next = kth_node
            new_tail.next = group_next

            # update group_prev and group_next
            group_prev = new_tail
            kth_node = get_kth(group_prev.next)
            group_next = kth_node.next if kth_node else None
    
        return dummy.next



# @lc code=end

