#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#

# @lc code=start
from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}

        def get_alice_max_stones(alice_turn: bool, i: int, M: int) -> int:
            if (alice_turn, i, M) in memo:
                return memo[(alice_turn, i, M)]
            if i >= n:
                return 0

            # If the current player can take all remaining piles
            if 2 * M >= n - i:
                if alice_turn:
                    # Alice gets all remaining stones
                    return sum(piles[i:])
                else:
                    # Bob takes them, Alice gets 0 more
                    return 0

            if not alice_turn:
                # Bob wants to MINIMIZE Alice's eventual result
                alice_min = float('inf')
                for bob_takes in range(1, min(2 * M, n - i) + 1):
                    alice_min = min(
                        alice_min,
                        get_alice_max_stones(True, i + bob_takes, max(M, bob_takes))
                    )
                memo[(alice_turn, i, M)] = alice_min
                return alice_min

            else:
                # Alice wants to MAXIMIZE her stones
                alice_max = 0
                additional = 0
                for alice_takes in range(1, min(2 * M, n - i) + 1):
                    additional += piles[i + alice_takes - 1]
                    alice_max = max(
                        alice_max,
                        additional + get_alice_max_stones(False, i + alice_takes, max(M, alice_takes))
                    )
                memo[(alice_turn, i, M)] = alice_max
                return alice_max

        return get_alice_max_stones(True, 0, 1)

# @lc code=end

