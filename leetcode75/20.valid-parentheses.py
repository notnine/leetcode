#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        opens = {'(','[','{'}
        stack = []

        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c == ')':
                    if top != '(':
                        return False
                if c == '}':
                    if top != '{':
                        return False
                if c == ']':
                    if top != '[':
                        return False
        
        return len(stack) == 0
# @lc code=end

