#
# @lc app=leetcode id=1574 lang=python3
#
# [1574] Shortest Subarray to be Removed to Make Array Sorted
#

# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        # find longest non decreasing subarr starting from index 0 (subarr a)
        j = 0
        while j+1 < n and arr[j] <= arr[j+1]:
            j += 1

        # find longest (reverted) non increasing subarr starting from index n-1 (subarr b)
        k = n - 1
        while k - 1 > j and arr[k] >= arr[k - 1]: # ensure a & b do not overlap
            k -= 1

        best = max(j + 1, (n - k)) # longest valid subarr
        # start with 0 elements added from prefix
        # while we can add elements from the prefix, add them. if we cannot add from prefix, remove from suffix
        # for every valid subarr we find, keep track of the best length so far
        i = 0 # ptr to number in prefix we are about to add

        while i <= j and k < n:
            print("i, k: " + str([i, k]))
            print("best: " + str(best))
            # if we can add from prefix, add it
            if arr[i] <= arr[k]:
                i += 1
                best = max(best, i + (n - k))
            # we cannot add from prefix so trim suffix
            else:
                k += 1

        return max(0, n - best)
# @lc code=end

