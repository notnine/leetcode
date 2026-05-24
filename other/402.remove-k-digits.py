#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [] # mono

        for c in num:
            while stack and stack[-1] > c and k > 0:
                stack.pop()
                k -= 1

            stack.append(c)
        
        # if we can still remove numbers, remove them from the end
        while k > 0:
            stack.pop()
            k -= 1
                
        # remove prepended 0s
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        res = ''.join(stack[i:])
        
        return res if res != '' else '0'
        

    def removeKdigits_archive(self, num: str, k: int) -> str:
        if k == len(num):
            return '0'
        
        memo = {}
        
        # backtracking, at index i, either we remove this num or we don't
        # given index i, and to_remove numbers to remove, return the smallest possible number
        def backtrack(i: int, to_remove: int, string: str) -> str:
            if (i, to_remove, string) in memo:
                return memo[(i, to_remove, string)]
            
            if i == len(num):
                return string
            
            if to_remove == 0:
                string = string + num[i:]
                memo[(i, to_remove, string)] = string
                return string

            # remove number at i
            removed = backtrack(i+1, to_remove - 1, string)

            # keep number at i
            kept = backtrack(i+1, to_remove, string + num[i])

            removed_int, kept_int = int(removed), int(kept)
            if removed_int < kept_int:
                memo[(i, to_remove, string)] = removed
            else:
                memo[(i, to_remove, string)] = kept

            return memo[(i, to_remove, string)]
        
        res = backtrack(0, k, '')
        # remove prepended 0s
        i = 0
        while i < len(res) and res[i] == '0':
            i += 1
        
        if res[i:] == '':
            return '0'
        else:
            return res[i:]
# @lc code=end

