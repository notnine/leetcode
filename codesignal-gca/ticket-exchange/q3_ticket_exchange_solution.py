"""
CodeSignal-style Q3 practice problem: Ticket Exchange Inventory

You run a ticket exchange platform. Tickets are grouped by event type.
For each event type, the platform stores ticket batches by price.

You must process a list of operations. There are 3 kinds of operations:

1) ["stock", eventType, price, quantity]
   Add `quantity` tickets of `eventType` at `price`.

2) ["sell", eventType, quantity]
   A customer wants to buy exactly `quantity` tickets of `eventType`.
   The platform must always sell the cheapest available tickets first.
   Return the total cost paid for this operation.

   If there are fewer than `quantity` tickets available for that event type,
   return -1 and do NOT change the inventory.

3) ["reprice", eventType, oldPrice, newPrice, quantity]
   Move exactly `quantity` tickets of `eventType` from `oldPrice` to `newPrice`.
   This is like changing the listed price of some tickets.

   If there are fewer than `quantity` tickets currently listed at `oldPrice`
   for that event type, ignore the operation.

Return a list containing the result of each "sell" operation, in order.

Notes
-----
- `eventType` is a string.
- `price`, `quantity` are positive integers.
- Repricing within the same price is allowed and should have no net effect.
- A sell operation must be all-or-nothing.
- After a price bucket reaches quantity 0, it should be treated as absent.

Example
-------
operations = [
    ["stock", "concert", 50, 4],
    ["stock", "concert", 30, 2],
    ["sell", "concert", 5],
    ["reprice", "concert", 50, 40, 1],
    ["sell", "concert", 2]
]

After the first two stock operations:
concert has {30: 2, 50: 4}

sell 5 -> take 2 tickets at 30 and 3 tickets at 50
cost = 2*30 + 3*50 = 210
remaining inventory: {50: 1}

reprice 1 ticket from 50 to 40 -> {40: 1}

sell 2 -> not enough inventory, return -1 and do not modify inventory

Answer: [210, -1]

Constraints
-----------
- 1 <= len(operations) <= 2 * 10^5
- 1 <= price, quantity <= 10^9
- Sum of successful inventory bucket updates can be large.

Target complexity
-----------------
Aim for roughly O(total_operations * log M + buckets_touched * log M),
where M is the number of active price buckets in one event type.

Suggested approach
------------------
For each event type:
- keep a hashmap: price -> quantity  (source of truth)
- keep a min-heap of prices
Use lazy deletion for stale heap entries.

Implement your solution in the function below.
"""

from typing import List, Any


def solution(operations: List[List[Any]]) -> List[int]:
    """Replace this stub with your solution."""
    raise NotImplementedError("Implement solution(operations)")
