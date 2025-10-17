#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#

# @lc code=start
class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.max_count = 0
        self.counts_to_nums = defaultdict(list) # maps a frequency to a list of nums, where those nums are at least that frequent

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.max_count = max(self.max_count, self.count[val])
        self.counts_to_nums[self.count[val]].append(val)

    def pop(self) -> int:
        # get num to pop
        num = self.counts_to_nums[self.max_count].pop()
        
        # if that group of counts is now empty
        if not self.counts_to_nums[self.max_count]:
            del self.counts_to_nums[self.max_count]
            self.max_count -= 1
        
        self.count[num] -= 1
        
        return num

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

