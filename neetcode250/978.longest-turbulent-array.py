class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # notice a turbulent array is where the nums go up down up down or down up down up

        res = 1
        down, up = 1, 1 # keeps track of the longest turbulent arr so far, where the last step was either down/up

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]: # last step was up
                up = down + 1
                res = max(res, up)
                down = 1

            elif arr[i] < arr[i-1]: # last step was down
                down = up + 1
                res = max(res, down)
                up = 1

            else: # no longer turbulent
                down, up = 1, 1
            
        return res
