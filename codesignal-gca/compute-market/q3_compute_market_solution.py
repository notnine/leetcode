"""
CodeSignal-style Q3 practice problem: Compute Capacity Marketplace

You run a marketplace for on-demand compute capacity. Capacity is grouped by
region. Within each region, capacity is listed in price buckets.

You must process a list of operations. There are 3 kinds of operations:

1) ["supply", region, price, units]
   Add `units` of capacity in `region` at `price`.

2) ["allocate", region, units]
   A customer wants to allocate exactly `units` of capacity from `region`.
   The platform must always allocate the cheapest available capacity first.
   Return the total cost for this operation.

   If there are fewer than `units` capacity units available in that region,
   return -1 and do NOT change the inventory.

3) ["rerate", region, oldPrice, newPrice, units]
   Move exactly `units` capacity units in `region` from `oldPrice` to `newPrice`.
   This represents repricing some existing listings.

   If there are fewer than `units` currently listed at `oldPrice` in that
   region, ignore the operation.

Return a list containing the result of each "allocate" operation, in order.

Notes
-----
- `region` is a string.
- `price`, `units` are positive integers.
- Rerating within the same price is allowed and should have no net effect.
- An allocate operation must be all-or-nothing.
- After a price bucket reaches quantity 0, it should be treated as absent.

Example
-------
operations = [
    ["supply", "us-east", 7, 3],
    ["supply", "us-east", 5, 2],
    ["allocate", "us-east", 4],
    ["rerate", "us-east", 7, 6, 1],
    ["allocate", "us-east", 2],
]

After the first two supply operations:
us-east has {5: 2, 7: 3}

allocate 4 -> take 2 units at 5 and 2 units at 7
cost = 2*5 + 2*7 = 24
remaining inventory: {7: 1}

rerate 1 unit from 7 to 6 -> {6: 1}

allocate 2 -> not enough inventory, return -1 and do not modify inventory

Answer: [24, -1]

Constraints
-----------
- 1 <= len(operations) <= 2 * 10^5
- 1 <= price, units <= 10^9
- Sum of successful inventory bucket updates can be large.

Target complexity
-----------------
Aim for roughly O(total_operations * log M + buckets_touched * log M),
where M is the number of active price buckets in one region.
"""

from typing import Any, List


def solution(operations: List[List[Any]]) -> List[int]:
    """Write your solution here."""
    raise NotImplementedError
