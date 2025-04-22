class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # return true if koko can eat all bananas with speed under h
        def valid(speed: int) -> bool:
            total_time = sum([math.ceil(pile / speed) for pile in piles])
            return total_time <= h
        
        l, r = 1, max(piles)
        m = (l + r) // 2

        while l < r:
            if valid(m): # "slow" koko down.
                r = m
            else: # "speed" koko up.
                l = m + 1
            m = (l + r) // 2
        
        return m

        # n = len(piles)
        # time O(n log(max(piles))
        # space O(1)
        