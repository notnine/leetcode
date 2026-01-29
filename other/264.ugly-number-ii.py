#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # we're just merging 3 sorted lists being ugly * 2, ugly * 3 and ugly * 5. but to save time, take the least product first

        ugly_nums = [1]
        i, j, k = 0, 0, 0
        count = 1

        while count != n:
            times_2 = ugly_nums[i] * 2
            times_3 = ugly_nums[j] * 3
            times_5 = ugly_nums[k] * 5

            min_product = min(times_2, times_3, times_5)
            
            # advance every ptr equal to min_product ot avoid duplicates
            i = i + 1 if times_2 == min_product else i
            j = j + 1 if times_3 == min_product else j
            k = k + 1 if times_5 == min_product else k

            ugly_nums.append(min_product)
            
            count += 1

        return ugly_nums[-1]
# @lc code=end

