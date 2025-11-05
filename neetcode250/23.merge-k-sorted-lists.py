#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = ListNode(0) # dummy head
        curr = res
        counter = 0 # break ties in the heap

        # init heap with head of each list
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, counter, l))
                counter += 1
        
        while heap:
            val, counter, node = heapq.heappop(heap)
            # if node.next, push into heap
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1
            # append node into res
            curr.next = node
            curr = curr.next
        
        return res.next
        
# @lc code=end

