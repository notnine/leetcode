class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use a non-increasing stack to keep track of the indices
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for index, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]: # curr temp is hotter than top of stack
                top_index = stack[-1]
                res[top_index] = index - top_index
                stack.pop()
            stack.append(index)

        return res

        # space & time O(n)