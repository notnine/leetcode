#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                b, a = stack.pop(), stack.pop()
                stack.append(str(int(a) + int(b)))
            elif c == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(str(int(a) - int(b)))
            elif c == '*':
                b, a = stack.pop(), stack.pop()
                stack.append(str(int(a) * int(b)))
            elif c == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(str(int(int(a) / int(b))))
            else:
                stack.append(c)
            
        return int(stack.pop())
# @lc code=end

