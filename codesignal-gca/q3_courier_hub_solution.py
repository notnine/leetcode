"""
CodeSignal-style Q3 practice problem: Courier Hub Dispatch

A courier company routes packages through multiple hubs.
Each hub stores pending packages, and dispatch requests must always ship
packages in strict priority order.

You must process a list of operations. There are 4 kinds:

1) ["ingest", hub, packageId, priority, units]
   Add `units` of package volume for `packageId` into `hub` with `priority`.

2) ["reschedule", hub, packageId, newPriority]
   Update the priority of an existing package in `hub`.
   If that package does not exist in that hub, ignore the operation.

3) ["cancel", hub, packageId, units]
   Remove exactly `units` from that package in that hub.
   If fewer than `units` are currently present, ignore the operation.
   If the package volume reaches 0, the package is removed.

4) ["dispatch", hub, units]
   Dispatch exactly `units` total volume from `hub`.
   Dispatch must always take from the lowest priority value first.
   If priorities tie, take lexicographically smaller packageId first.

   Return the total dispatch cost:
     sum(units_taken * priority) across all taken package chunks.

   If there are fewer than `units` total volume in that hub,
   return -1 and do NOT modify that hub.

Return a list containing the result of each "dispatch" operation, in order.

Notes
-----
- `hub`, `packageId` are non-empty strings.
- `priority`, `units`, `newPriority` are positive integers.
- A packageId appears at most once per hub at any moment.
- Rescheduling to the same priority is allowed and is a no-op.

Example
-------
operations = [
    ["ingest", "north", "pkgA", 4, 3],
    ["ingest", "north", "pkgB", 2, 2],
    ["dispatch", "north", 4],
    ["reschedule", "north", "pkgA", 1],
    ["ingest", "north", "pkgC", 3, 2],
    ["dispatch", "north", 2],
]

After first two operations:
north has:
  pkgA -> (priority=4, units=3)
  pkgB -> (priority=2, units=2)

dispatch 4:
  take 2 from pkgB (2*2)
  take 2 from pkgA (2*4)
cost = 12
remaining:
  pkgA -> (priority=4, units=1)

reschedule pkgA to priority 1
ingest pkgC with priority 3, units 2

dispatch 2:
  take 1 from pkgA (1*1)
  take 1 from pkgC (1*3)
cost = 4

Answer: [12, 4]

Constraints
-----------
- 1 <= len(operations) <= 2 * 10^5
- 1 <= priority, units <= 10^9
- Many operations may target the same hub/package.

Target complexity
-----------------
Aim for O(N log M), where:
- N is number of operations
- M is number of active packages in one hub

Hint:
Use hash maps for authoritative package state and a min-heap with lazy
deletion for dispatch order.
"""

from typing import Any, List
import heapq
from collections import defaultdict

def solution(operations: List[List[Any]]) -> List[int]:
  hub_to_heap = defaultdict(list) # hub -> min heap of [prio, packageId]
  hub_to_freq_dict = defaultdict(dict) # hub -> packageId: [prio, units]
  res = []

  for operation in operations:
    op = operation[0]

    if op == "ingest":
      hub, package_id, prio, units = operation[1], operation[2], operation[3], operation[4]
      heap = hub_to_heap[hub]
      freq_dict = hub_to_freq_dict[hub]

      # if a different prio exist, no op
      if package_id in freq_dict and freq_dict[package_id][0] != prio:
        continue

      heapq.heappush(heap, [prio, package_id])
      if package_id not in freq_dict:
        freq_dict[package_id] = [prio, units]
      else:
        freq_dict[package_id][1] += units

    
    elif op == "reschedule":
      hub, package_id, new_prio = operation[1], operation[2], operation[3]
      freq_dict = hub_to_freq_dict[hub]
      heap = hub_to_heap[hub]

      if package_id not in freq_dict:
        continue
      
      if freq_dict[package_id][0] == new_prio:
        continue
      
      units = freq_dict[package_id][1]
      freq_dict[package_id] = [new_prio, units]
      heapq.heappush(heap, [new_prio, package_id])
      

    elif op == "cancel":
      hub, package_id, units = operation[1], operation[2], operation[3]
      freq_dict = hub_to_freq_dict[hub]

      if package_id not in freq_dict:
        continue

      elif freq_dict[package_id][1] < units:
        continue
      
      elif freq_dict[package_id][1] == units:
        del freq_dict[package_id]
      
      else:
        freq_dict[package_id][1] -= units

      
    elif op == "dispatch":
      hub, to_dispatch = operation[1], operation[2]
      freq_dict = hub_to_freq_dict[hub] # packageId: (prio, units)
      heap = hub_to_heap[hub] # min heap of (prio, packageId)

      total_units = 0
      for package_id in freq_dict:
        total_units += freq_dict[package_id][1]
      if total_units < to_dispatch:
        res.append(-1)
        continue
        
      taken_so_far = 0
      total_cost = 0

      while taken_so_far < to_dispatch:
        # check that this isn't a stale heap entry
        while True:
          prio, package_id = heapq.heappop(heap)
          if package_id not in freq_dict:
            continue
          accurate_prio, accurate_units = freq_dict[package_id]
          if accurate_prio == prio:
            break

        available_units = freq_dict[package_id][1]
        to_take = min(available_units, to_dispatch - taken_so_far)

        if to_take == available_units:
          del freq_dict[package_id]
        else:
          heapq.heappush(heap, [prio, package_id])          
          freq_dict[package_id][1] -= to_take
        
        taken_so_far += to_take
        total_cost += prio * to_take
      
      res.append(total_cost)

  return res