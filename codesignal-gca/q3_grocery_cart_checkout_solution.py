"""
CodeSignal-style Q3 practice problem: Grocery Cart Checkout

A supermarket manages inventory by department. In each department, every item
has:
- a current unit price
- a current quantity in stock

You must process a list of operations:

1) ["restock", department, item, price, quantity]
  Add inventory for one item.
  - If item does not exist in this department: create it with (price, quantity).
  - If item exists with the same price: increase quantity.
  - If item exists with a different price: ignore operation (invalid input).

2) ["reprice", department, item, newPrice]
  Change the item's price in that department.
  - If item does not exist: ignore.
  - If newPrice equals current price: no-op.

3) ["remove", department, item, quantity]
  Remove exactly `quantity` from item stock.
  - If item does not exist: ignore.
  - If current quantity < quantity: ignore.
  - If quantity becomes 0, remove the item.

4) ["purchase", department, quantity]
  A customer wants exactly `quantity` units from this department.
  Purchase order:
  - always take the lowest price first
  - if prices tie, take lexicographically smaller item first

  Return total purchase cost:
    sum(units_taken * price)

  If total stock in the department is less than `quantity`:
  - return -1
  - do NOT mutate that department

Return a list of results for each "purchase" operation, in order.

Notes
-----
- An item appears at most once per department in current state.
- department and item are non-empty strings.
- price and quantity are positive integers.
- If you use a heap, stale heap entries are expected and should be handled
  with lazy deletion against authoritative state.

Example
-------
operations = [
    ["restock", "produce", "apple", 3, 4],
    ["restock", "produce", "banana", 2, 3],
    ["purchase", "produce", 5],
    ["reprice", "produce", "apple", 1],
    ["restock", "produce", "carrot", 4, 2],
    ["remove", "produce", "carrot", 1],
    ["purchase", "produce", 2]
]

After first two restocks:
produce has:
  banana -> (2,3)
  apple  -> (3,4)

purchase 5:
  take 3 banana (3*2)
  take 2 apple  (2*3)
cost = 12
remaining:
  apple -> (3,2)

reprice apple to 1
restock carrot (4,2), remove 1 -> carrot (4,1)

purchase 2:
  take 2 apple (2*1)
cost = 2

Answer: [12, 2]

Constraints
-----------
- 1 <= len(operations) <= 2 * 10^5
- 1 <= price, quantity <= 10^9

Target complexity
-----------------
Aim for approximately O(N log M), where:
- N = number of operations
- M = number of active items in one department
"""

from typing import Any, List
import heapq
from collections import defaultdict

def solution(operations: List[List[Any]]) -> List[int]:
  dept_to_dict = defaultdict(dict) # dept -> {item: [price, quantity]}
  dept_to_heap = defaultdict(list) # dept -> min heap [(price, item)]
  dept_to_stock = defaultdict(int) # dept -> total num of items
  res = []

  for op in operations:

    if op[0] == "restock":
      dept, item, price, quantity = op[1], op[2], op[3], op[4]
      hashmap, heap = dept_to_dict[dept], dept_to_heap[dept]

      if item not in hashmap:
        hashmap[item] = [price, quantity]
        heapq.heappush(heap, (price, item))
        dept_to_stock[dept] += quantity
      
      else:
        if hashmap[item][0] == price:
          hashmap[item][1] += quantity
          dept_to_stock[dept] += quantity
        else:
          continue

    elif op[0] == "reprice":
      dept, item, new_price = op[1], op[2], op[3]
      hashmap, heap = dept_to_dict[dept], dept_to_heap[dept]

      if item not in hashmap:
        continue
      
      if hashmap[item][0] == new_price:
        continue

      hashmap[item][0] = new_price
      heapq.heappush(heap, (new_price, item))

    elif op[0] == "remove":
      dept, item, quantity = op[1], op[2], op[3]
      hashmap, heap = dept_to_dict[dept], dept_to_heap[dept]

      if item not in hashmap:
        continue
      
      if hashmap[item][1] < quantity:
        continue
      
      hashmap[item][1] -= quantity
      if hashmap[item][1] == 0:
        del hashmap[item]
      dept_to_stock[dept] -= quantity

    else:
      dept, quantity = op[1], op[2]
      hashmap, heap = dept_to_dict[dept], dept_to_heap[dept]

      if dept_to_stock[dept] < quantity:
        res.append(-1)
        continue
      
      taken_so_far = 0
      cost_so_far = 0

      # dept_to_dict = defaultdict(dict) # dept -> {item: [price, quantity]}
      # dept_to_heap = defaultdict(list) # dept -> min heap [(price, item)]
      # dept_to_stock = defaultdict(int) # dept -> total num of items

      while taken_so_far < quantity:
        price, item = heapq.heappop(heap)

        # if stale
        if item not in hashmap or hashmap[item][0] != price:
          continue
        
        to_take = min(hashmap[item][1], quantity - taken_so_far)
        cost_so_far += to_take * price
        taken_so_far += to_take

        hashmap[item][1] -= to_take
        if hashmap[item][1] > 0:
          heapq.heappush(heap, (price, item))
        if hashmap[item][1] == 0:
          del hashmap[item]
      
      dept_to_stock[dept] -= quantity
      res.append(cost_so_far)

  return res
