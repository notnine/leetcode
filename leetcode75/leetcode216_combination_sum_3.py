class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        curr = []
        nums = [1,2,3,4,5,6,7,8,9]

        def backtrack(i: int) -> None:
            if len(curr) == k and sum(curr) == n:
                res.append(curr.copy())
                return
            if len(curr) == k and sum(curr) != n:
                return
            # we've used numbers 0 to i - 1, try with i to 8
            for index in range(i, 9):
                curr.append(nums[index])
                backtrack(index + 1)
                curr.pop()

        backtrack(0)
        return res
