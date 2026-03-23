#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
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
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def get_gcd(num_1: int, num_2: int) -> int:
            # euclidian algo
            while num_2 != 0:
                num_1, num_2 = num_2, num_1 % num_2
            return num_1


        prev = head
        curr = head.next

        while curr is not None: # len(LL)
            # 0. get gcd between prev & curr
            gcd = get_gcd(prev.val, curr.val) # runtime: max num in LL

            # 1. insert a new node b/w prev & curr of gcd
            new_node = ListNode(val=gcd, next=curr)
            prev.next = new_node

            # 2. update prev & curr
            prev = curr
            curr = prev.next

        return head

        # runtime O(len(LL) * max num in LL)
# @lc code=end

