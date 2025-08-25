#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1 for _ in range(k)]
        self.front = 0 # points to the index of the first element (unless emtpy)
        self.back = 0 # points to the index of the last element (unless empty)
        self.n = k
        self.size = 0 # curr size of circular queue

    def enQueue(self, value: int) -> bool:
        if self.size == self.n:
            return False
        
        if self.size == 0:
            self.queue[self.back] = value
        else:
            back_index = self.back + 1
            if back_index == self.n: back_index = 0
            self.queue[back_index] = value
            self.back = back_index

        self.size += 1
        return True


    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        elif self.size == 1:
            self.queue[self.front] = -1
            self.size -= 1
            return True
        else:
            self.queue[self.front] = -1
            self.front += 1
            if self.front == self.n: self.front = 0
            self.size -= 1
            return True


    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.back]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.n
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

