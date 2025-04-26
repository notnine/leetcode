from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_deque = deque()
        d_deque = deque()
        n = len(senate)

        for i in range(len(senate)):
            if senate[i] == 'R':
                r_deque.append(i)
            else:
                d_deque.append(i)

        while r_deque and d_deque:
            curr_r = r_deque.popleft()
            curr_d = d_deque.popleft()
            if curr_r < curr_d: # curr_r bans curr_d
                r_deque.append(curr_r + n)
            else:
                d_deque.append(curr_d + n)
        
        return "Radiant" if r_deque else "Dire"

        # O(n) space & time