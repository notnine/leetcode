#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
from collections import defaultdict

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left) # dummy nodes to avoid edge cases
        self.left.next = self.right
        self.map = {} # maps val to node

    def length(self):
        return len(self.map)
    
    # append new node just before dummy right node
    def push_right(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev.next = node
        self.right.prev = node

    # pop val from LL
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            nxt, prev = node.next, node.prev
            nxt.prev = prev
            prev.next = nxt
            del self.map[val]

    # pop LRU (tail)
    def pop_left(self):
        if self.left.next is self.right: # empty LL
            return None
        node = self.left.next
        self.pop(node.val)
        return node.val

    # udpate val to be MRU
    def update(self, val):
        self.pop(val)
        self.push_right(val)

class LFUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.lfu_count = 0
        self.key_to_val = {} # maps key to val
        self.key_to_count = defaultdict(int) # maps key to count
        self.freq_to_list = defaultdict(LinkedList) # maps freq to LL of keys ordered by recency
    
    def counter(self, key):
        count = self.key_to_count[key]
        self.key_to_count[key] += 1
        self.freq_to_list[count].pop(key) # remove from old freq's LL

        # if original lfu count has no more nodes in its LL
        if count == self.lfu_count and self.freq_to_list[count].length() == 0:
            self.lfu_count += 1

        self.freq_to_list[count + 1].push_right(key) # add to new freq's LL

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        self.counter(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.c == 0:
            return

        if key in self.key_to_val:
            # udpate val & bump freq
            self.key_to_val[key] = value
            self.counter(key)
            return
        
        # evict if full
        if len(self.key_to_val) == self.c:
            key_to_evict = self.freq_to_list[self.lfu_count].pop_left()
            if key_to_evict is not None:
                self.key_to_val.pop(key_to_evict, None)
                self.key_to_count.pop(key_to_evict, None)

        # insert new key w/ freq 1
        self.key_to_val[key] = value
        self.key_to_count[key] = 1
        self.freq_to_list[1].push_right(key)
        self.lfu_count = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

