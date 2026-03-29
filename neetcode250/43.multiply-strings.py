#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        
        list1, list2 = list(num1)[::-1], list(num2)[::-1]

        res = [0] * (len(list1)+len(list2))

        # list2 is shorter, and is placed at the "bottom" in the mult. board
        for j in range(len(list2)):
            for i in range(len(list1)):
                product = int(list2[j])*int(list1[i]) + res[i+j]
                res[i+j] = product % 10
                res[i+j+1] += product // 10

        for i in range(len(res)):
            res[i] = str(res[i])

        res = res[::-1]
        i = 0 # first non zero index
        while res[i] == '0':
            i += 1
        res = ''.join(res[i:])

        return res
# @lc code=end

