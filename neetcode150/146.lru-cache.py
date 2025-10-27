#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev_node = None
        self.next_node = None

class LRUCache:
    def __init__(self, capacity: int):
        self.c = capacity
        self.keyToNode = {}
        self.head = None  # MRU
        self.tail = None  # LRU

    def remove_node(self, node: Node) -> None:
        if node.prev_node:
            node.prev_node.next_node = node.next_node
        else:
            self.tail = node.next_node
            if self.tail:
                self.tail.prev_node = None

        if node.next_node:
            node.next_node.prev_node = node.prev_node
        else:
            self.head = node.prev_node
            if self.head:
                self.head.next_node = None

        del self.keyToNode[node.key]

    def add_node(self, node: Node) -> None:
        node.prev_node = self.head
        node.next_node = None

        if self.head:
            self.head.next_node = node
        self.head = node

        if not self.tail:
            self.tail = node

        self.keyToNode[node.key] = node

        if len(self.keyToNode) > self.c:
            self.remove_node(self.tail)

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1
        node = self.keyToNode[key]
        self.remove_node(node)
        self.add_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.remove_node(self.keyToNode[key])
        new_node = Node(key, value)
        self.add_node(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

