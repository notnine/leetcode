#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n == -1:
            return 1/x
        elif n == 0:
            return 1
        
        # 3^4 = 3*3*3*3 = 3^2 * 3^2 # so notice we can just calc. 3^2 once, shaving it down to O(logn)
        if n > 1:
            if n % 2 == 0:
                pow_half = self.myPow(x, n//2)
                return pow_half * pow_half
            else:
                compute = self.myPow(x, n-1)
                return x * compute
        else:
            if n % 2 == 0:
                # flip n to positive
                n *= -1
                pow_half = self.myPow(x, n//2)
                return 1/(pow_half * pow_half)
            else:
                # flip n to positive
                n *= -1
                compute = self.myPow(x, n-1)
                return 1/(x * compute)

# @lc code=end

