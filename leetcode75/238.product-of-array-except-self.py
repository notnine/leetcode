#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1] # prefix_products[i] = the postfix products including at i
        postfix_products = [] # postfix_products[i] = the postfix products from len(n) - 1 to i including i

        running_product = 1
        for num in nums:
            running_product *= num
            prefix_products.append(running_product)
        
        running_product = 1
        for num in nums[::-1]:
            running_product *= num
            postfix_products.append(running_product)
        postfix_products.reverse()
        postfix_products.append(1)

        res = []
        for i in range(len(nums)):
            product = postfix_products[i+1] * prefix_products[i]
            res.append(product)
        return res


# @lc code=end

