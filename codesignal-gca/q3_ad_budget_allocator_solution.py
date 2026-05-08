"""
CodeSignal-style Q3 practice problem: Library Clearance Checkout

A library is clearing out old inventory. Books are grouped by genre.
Within each genre, each title has:
- a current unit price
- a number of copies available

Process a list of operations:

1) ["stock", genre, title, price, copies]
   Add copies of a title.
   - If title does NOT exist in that genre: create it with (price, copies).
   - If title exists with the same price: increase copies.
   - If title exists with a different price: ignore operation (invalid input).

2) ["relabel", genre, title, newPrice]
   Change the price of an existing title in that genre.
   - If title does not exist: ignore.
   - If newPrice equals current price: no-op.

3) ["discard", genre, title, copies]
   Remove exactly `copies` from that title in that genre.
   - If title does not exist: ignore.
   - If available copies < copies: ignore.
   - If copies become 0, remove the title from the genre.

4) ["checkout", genre, copies]
   A buyer wants exactly `copies` books from this genre.
   Selection rules:
   - take lowest price first
   - if prices tie, take lexicographically smaller title first

   Return total checkout cost:
     sum(copies_taken * price)

   If the genre has fewer than `copies` total available books:
   - return -1
   - do NOT mutate that genre

Return a list containing the result of each "checkout" operation, in order.

Notes
-----
- A title appears at most once per genre in current state.
- `genre` and `title` are non-empty strings.
- `price` and `copies` are positive integers.
- If you use a heap, stale entries are expected and should be handled with
  lazy deletion against authoritative state.

Example
-------
operations = [
    ["stock", "fantasy", "Mistborn", 8, 3],
    ["stock", "fantasy", "Hobbit", 5, 2],
    ["checkout", "fantasy", 4],
    ["relabel", "fantasy", "Mistborn", 4],
    ["stock", "fantasy", "Narnia", 6, 2],
    ["discard", "fantasy", "Narnia", 1],
    ["checkout", "fantasy", 2]
]

After first two stock operations:
fantasy has:
  Hobbit   -> (price=5, copies=2)
  Mistborn -> (price=8, copies=3)

checkout 4:
  take 2 Hobbit (2*5)
  take 2 Mistborn (2*8)
cost = 26
remaining:
  Mistborn -> (8,1)

relabel Mistborn to 4
stock Narnia (6,2), then discard 1 => Narnia (6,1)

checkout 2:
  take 1 Mistborn (1*4)
  take 1 Narnia  (1*6)
cost = 10

Answer: [26, 10]

Constraints
-----------
- 1 <= len(operations) <= 2 * 10^5
- 1 <= price, copies <= 10^9

Target complexity
-----------------
Aim for about O(N log M), where:
- N = number of operations
- M = number of active titles in one genre
"""

from typing import Any, List
from collections import defaultdict
import heapq

def solution(operations: List[List[Any]]) -> List[int]:
    genre_to_hashmap = defaultdict(dict)# genre -> {title: [price, copies]}
    genre_to_heap = defaultdict(list) # genre -> heap (price, title)
    genre_to_total_books = defaultdict(int) # genre -> total num of books
    res = []

    for op in operations:
        
        if op[0] == "stock":
            genre, title, price, copies = op[1], op[2], op[3], op[4]
            hashmap, heap = genre_to_hashmap[genre], genre_to_heap[genre]

            if title not in hashmap:
                hashmap[title] = [price, copies]
                heapq.heappush(heap, (price, title))
                genre_to_total_books[genre] += copies
            else:
                if hashmap[title][0] == price:
                    hashmap[title][1] += copies
                    genre_to_total_books[genre] += copies
                else: # title exists with different price, ignore op
                    continue
        
        elif op[0] == "relabel":
            genre, title, new_price = op[1], op[2], op[3]
            hashmap, heap = genre_to_hashmap[genre], genre_to_heap[genre]

            if title not in hashmap:
                continue
            
            if hashmap[title][0] == new_price:
                continue
            
            hashmap[title][0] = new_price
            heapq.heappush(heap, (new_price, title))
            # heap will contain stale price, but will be lazily removed in checkout
        
        elif op[0] == "discard":
            genre, title, copies = op[1], op[2], op[3]
            hashmap, heap = genre_to_hashmap[genre], genre_to_heap[genre]

            if title not in hashmap:
                continue
            
            if hashmap[title][1] < copies:
                continue
            
            if hashmap[title][1] == copies:
                del hashmap[title]
            else:
                hashmap[title][1] -= copies

            genre_to_total_books[genre] -= copies

        else:
            # genre_to_hashmap = defaultdict(dict)# genre -> {title: [price, copies]}
            # genre_to_heap = defaultdict(list) # genre -> heap (price, title)
            # genre_to_total_books = defaultdict(int) # genre -> total num of books
            genre, to_checkout = op[1], op[2]
            hashmap, heap = genre_to_hashmap[genre], genre_to_heap[genre]
            
            if genre_to_total_books[genre] < to_checkout:
                res.append(-1)
                continue
            
            checked_out = 0
            check_out_cost = 0

            while checked_out < to_checkout:
                price, title = heapq.heappop(heap)

                # if stale, continue
                if title not in hashmap or hashmap[title][0] != price:
                    continue
                
                avail_copies = hashmap[title][1]
                to_take = min(avail_copies, to_checkout - checked_out)
                remaining_copies = avail_copies - to_take
                checked_out += to_take
                check_out_cost += to_take * price


                if remaining_copies > 0:
                    heapq.heappush(heap, (price, title))
                    hashmap[title][1] = remaining_copies
                else:
                    del hashmap[title]
                
            genre_to_total_books[genre] -= to_checkout
            res.append(check_out_cost)
            
    return res
