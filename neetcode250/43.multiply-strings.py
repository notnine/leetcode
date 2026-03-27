#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        
        list1, list2 = list(num1)[::-1], list(num2)[::-1]

        # todo: we're just continuing to append to the list, we need to actually "add" to the res. use indices, it will help.
        carry = 0
        res = []
        for i in list2:
            for j in list1:
                res.append(str((int(i) * int(j) + carry) % 10)) # last bit goes into res
                carry = (int(i) * int(j) + carry) // 10 # first bit goes into carry
            #

        res = ''.join(res[::-1])
        if carry > 0:
            res = str(carry) + res

        return res
# @lc code=end

