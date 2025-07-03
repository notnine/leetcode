#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap:
    size = 1000001
    def __init__(self):
        self.data = [[] for _ in range(MyHashMap.size + 1)] # buckets containing (key, value)

    def put(self, key: int, value: int) -> None:
        index = key % MyHashMap.size # our hash

        # traverse through key-val pairs in bucket @ index
        for i, (k, v) in enumerate(self.data[index]):
            if k == key: # if key exists, overwrite its value
                self.data[index][i] = (k, value)
                return
        # key does not exist, append new key-value pair to current bucket
        self.data[index].append((key, value))

    def get(self, key: int) -> int:
        index = key % MyHashMap.size

        for k, v in self.data[index]:
            if k == key:
                return v

        return -1        

    def remove(self, key: int) -> None:
        # if we encounter lots of collisions our bucket could get long
        # to obtain O(1) time for remove, swap key-val pair with the last index before removing
        index = key % MyHashMap.size
        print("Bucket contents:", self.data[index])
        for i, (k,v) in enumerate(self.data[index]):
            if k == key: # swap with last, then remove this key-val pair
                self.data[index][i], self.data[index][-1] = self.data[index][-1], self.data[index][i]
                self.data[index].pop()

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

