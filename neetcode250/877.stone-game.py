#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        # given the game state, return whether alice wins. pre-req: l & r are in bounds
        def dp(alice_points: int, bob_points: int, alice_turn: bool, l: int, r: int) -> bool:
            if l == r:
                if alice_turn:
                    alice_points += piles[l]
                else:
                    bob_points += piles[l]
                return alice_points > bob_points
            
            if alice_turn:
                # alice takes head
                take_head = dp(alice_points + piles[l], bob_points, not alice_turn, l + 1, r)
                # alice takes tail
                take_tail = dp(alice_points + piles[r], bob_points, not alice_turn, l, r - 1)
                return take_head or take_tail
            else:
                # bob takes head
                take_head = dp(alice_points, bob_points + piles[l], not alice_turn, l + 1, r)
                # bob takes tail
                take_tail = dp(alice_points, bob_points + piles[r], not alice_turn, l, r - 1)
                return take_head or take_tail

        return dp(0, 0, True, 0, len(piles) - 1)
# @lc code=end

