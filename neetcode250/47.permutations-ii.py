#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        
        # pre-req: arr is sorted
        def permutate(arr: List[int]) -> List[List[int]]:
            if not arr:
                return [[]]
            
            if len(arr) == 1:
                return [arr]

            # take each element from arr, permutate arr, append element to the back
            # do not permutate if taken element is a duplicate.
            n = len(arr)
            i = 0
            res = []
            while i < n:
                # take element at i
                num = arr[i]

                # permutate the rest of the arr
                curr = arr[:i] + arr[i+1:]
                permutations = permutate(curr)

                # append element to the back
                for permutation in permutations:
                    permutation.append(num)
                
                res.extend(permutations)

                # skip i to the next unique element to avoid duplicates
                i += 1
                while i < n and arr[i] == arr[i-1]:
                    i += 1
                
            return res

        nums.sort()
        return permutate(nums)
# @lc code=end

