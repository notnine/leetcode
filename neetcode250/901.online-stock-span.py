#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            self.span.append(1)
            return 1

        self.stack.append(price)
        i = len(self.stack) - 2

        # find index of last time a price was higher than today's
        while i >= 0 and self.stack[i] <= price:
            i = i - self.span[i]

        self.span.append(len(self.stack) - 1 - i)
        return len(self.stack) - 1 - i



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

