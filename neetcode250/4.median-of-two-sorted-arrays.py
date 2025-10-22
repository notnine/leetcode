#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # ensure A is the shorter arr
        if len(A) > len(B):
            A, B = B, A
        n, m = len(A), len(B)
        total = n + m
        first_half_len = (total // 2) # number of elements at first half

        # run bin search where search space is 0,.. n. we want to partition A & B such that our partition contains the left partition of the merged arr.
        # therefore we need to figure out at which index we need to partition A. Let i, j be the points in which we split A & B.

        l, r = 0, n - 1

        while True:
            i = (l + r) // 2 # index of final element at leftA
            j = first_half_len - i - 2

            # get the values of the borders of our partitions, which we will use to validate our partition.
            leftA = A[i] if i >= 0 else -float('inf') # because if out of bounds, it means we want our partition to be all from B in this case.
            rightA = A[i + 1] if i + 1 < n else float('inf')
            leftB = B[j] if j >= 0 else -float('inf')
            rightB = B[j + 1] if j + 1 < m else float('inf')

            # if valid partition, compute & return median
            if leftA <= rightB and leftB <= rightA:
                # if even len
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            
            # if not valid partition
            else:
                if leftA > rightB:
                    # then we need to decrease A
                    r = i - 1

                else: # leftB > rightA
                    # we need to increase A
                    l = i + 1
                
# @lc code=end
