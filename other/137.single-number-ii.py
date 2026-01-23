#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res[i] will count how many times bit i (LSB = 0) is set
        res = [0] * 32

        for num in nums:
            # 32-bit two's complement representation
            bin_num = format(num & 0xffffffff, '032b')[::-1]  # reverse so index 0 = LSB

            for i, bit in enumerate(bin_num):
                res[i] += int(bit)

        # rebuild the unique number from bits mod 3
        for i in range(32):
            res[i] %= 3

        # convert bits back to integer
        res_bits = "".join(str(bit) for bit in res[::-1])  # reverse back to MSB first
        ans = int(res_bits, 2)

        # handle negative numbers (two's complement)
        if ans >= 2**31:
            ans -= 2**32

        return ans

# @lc code=end

