"""
CodeSignal-style Q3 practice problem: Checkout Counter Assignment

A supermarket has multiple checkout counters. Each counter has a fixed
"efficiency score" (lower is better). Customers arrive over time and each one
takes a certain number of seconds to check out.

You must assign each arriving customer to a counter using these rules:

1) Customer i arrives at time i (0-indexed by the input array).
2) If one or more counters are free at arrival time:
   - assign the customer to the free counter with the smallest efficiency score
   - tie-break by smaller counter index
3) If no counters are free:
   - the customer waits until at least one counter becomes free
   - then assign to the best available counter by the same priority
4) Once assigned at time t, a counter is busy until t + checkoutTime[i].

Return an array `assigned`, where `assigned[i]` is the index of the counter
that serves customer i.

Function signature
------------------
solution(counterEfficiency: List[int], checkoutTime: List[int]) -> List[int]

Input
-----
- `counterEfficiency[j]` is the efficiency score for counter j (lower is better)
- `checkoutTime[i]` is the processing time for customer i

Example
-------
counterEfficiency = [3, 1, 4]
checkoutTime = [5, 2, 3, 4, 1]

Customer 0 arrives at t=0:
- all counters are free, best is counter 1 (score 1)
- assign customer 0 to counter 1, busy until t=5

Customer 1 arrives at t=1:
- free counters: 0 (score 3), 2 (score 4)
- assign to counter 0, busy until t=3

Customer 2 arrives at t=2:
- free counters: 2 only
- assign to counter 2, busy until t=5

Customer 3 arrives at t=3:
- counter 0 just became free
- assign to counter 0, busy until t=7

Customer 4 arrives at t=4:
- no counters free (counter 1 busy to 5, counter 2 busy to 5, counter 0 busy to 7)
- wait to t=5, counters 1 and 2 become free
- pick best free counter: 1

Answer: [1, 0, 2, 0, 1]

Constraints
-----------
- 1 <= len(counterEfficiency) <= 2 * 10^5
- 1 <= len(checkoutTime) <= 2 * 10^5
- 1 <= counterEfficiency[j], checkoutTime[i] <= 10^9

Target complexity
-----------------
Aim for O((N + M) log M), where:
- N = number of customers
- M = number of counters

Hint
----
Use two heaps:
- available counters by (efficiency, index)
- busy counters by (free_time, efficiency, index)
"""

from typing import List
from collections import defaultdict
import heapq

def solution(counterEfficiency: List[int], checkoutTime: List[int]) -> List[int]:

   res = []

   available_counters = [] # heap (efficiency, counter)
   busy_counters = [] # heap (time_freed, efficiency, counter)


   for counter, efficiency in enumerate(counterEfficiency):
      heapq.heappush(available_counters, (efficiency, counter))

   t = 0

   for customer, checkout_time in enumerate(checkoutTime):
      t = max(t, customer) # don't go backward in time

      while busy_counters and t >= busy_counters[0][0]:
         _, efficiency, counter = heapq.heappop(busy_counters)
         heapq.heappush(available_counters, (efficiency, counter))

      if available_counters:
         efficiency, counter = heapq.heappop(available_counters)
         res.append(counter)
         heapq.heappush(busy_counters, (t + checkout_time, efficiency, counter))

      else: # customer needs wait, pop the next 
         time_freed, efficiency, counter = heapq.heappop(busy_counters)
         heapq.heappush(available_counters, (efficiency, counter))

         while busy_counters and busy_counters[0][0] == time_freed:
            time_freed, efficiency, counter = heapq.heappop(busy_counters)
            heapq.heappush(available_counters, (efficiency, counter))

         eff, counter = heapq.heappop(available_counters)
         res.append(counter)
         heapq.heappush(busy_counters, (time_freed + checkout_time, eff, counter))

   return res
