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
from collections import defaultdict
import heapq

def solution(operations: List[List[Any]]) -> List[int]:
   # ds to maintain
   # a. dictionary region -> dictionary price -> units
   region_to_price_units = defaultdict(dict)
   # b. dictionary region -> min heap of prices (lazy deletion)
   region_to_min_heap = defaultdict(list)
   # c. dictionary region -> total units available
   region_to_total_units = defaultdict(int)
   res = []

   for operation in operations:
      op = operation[0]

      # supply
      # upadte a, b, c
      if op == "supply":
         region, price, units = operation[1], operation[2], operation[3]
         a, b, c = region_to_price_units[region], region_to_min_heap[region], region_to_total_units[region]
         # update b
         if price not in a:
            heapq.heappush(b, price)
         # update a
         if price not in a:
            a[price] = units
         else:
            a[price] += units
         # update c
         region_to_total_units[region] += units

      # allocate
      # update a, b (if min price no longer avail, delete), c, res
      elif op == "allocate":
         region, units = operation[1], operation[2]
         a, b, c = region_to_price_units[region], region_to_min_heap[region], region_to_total_units[region]
         # if impossible skip
         if c < units:
            res.append(-1)
            continue
         amount_taken = 0
         total_price = 0
         while b and amount_taken < units:
            min_price = heapq.heappop(b)
            if a.get(min_price, 0) == 0:
               continue
            else:
               amount_available = a.get(min_price, 0)
               amount_to_take = min(amount_available, units - amount_taken)
               total_price += amount_to_take * min_price
               a[min_price] -= amount_to_take
               if a[min_price] == 0:
                  del a[min_price]
               amount_taken += amount_to_take
               if amount_to_take < amount_available:
                  heapq.heappush(b, min_price)
         region_to_total_units[region] -= units
         res.append(total_price)

      # rerate
      # update a, b
      elif op == "rerate":
         region, old_price, new_price, units = operation[1], operation[2], operation[3], operation[4]
         if old_price == new_price:
            continue
         a, b, c = region_to_price_units[region], region_to_min_heap[region], region_to_total_units[region]
         # if impossible skip
         if a.get(old_price, 0) < units:
            continue
         
         # update b (min heap) if new_price is new
         if a.get(new_price, 0) == 0:
            heapq.heappush(b, new_price)

         # update a
         a[old_price] -= units
         if a.get(old_price, 0) == 0:
            del a[old_price]
         if new_price not in a:
            a[new_price] = units
         else:
            a[new_price] += units
      
   return res