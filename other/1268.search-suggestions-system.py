#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        i = 1 # pointer to searchWord

        while i <= len(searchWord):
            curr_prefix = searchWord[:i]
            curr_suggestions = []
            # do our logic, append to curr_suggestions
            for product in products:
                # if product starts with curr_prefix, append to curr_suggestions
                if product.startswith(curr_prefix):
                    curr_suggestions.append(product)
                if len(curr_suggestions) == 3:
                    break

            # update res, i
            res.append(curr_suggestions)
            i += 1

        return res


# @lc code=end
