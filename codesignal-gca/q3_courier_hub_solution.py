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


def solution(operations: List[List[Any]]) -> List[int]:
    raise NotImplementedError("Implement this Q3 practice problem.")
