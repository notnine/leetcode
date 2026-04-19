from typing import List, Any
from collections import defaultdict
import heapq


def solution(operations: List[List[Any]]) -> List[int]:
    res = []

    # event -> {price: quantity}
    event_to_price_quantity = defaultdict(dict)

    # event -> min-heap of prices
    event_to_min_heap = defaultdict(list)

    # event -> total quantity across all prices
    event_to_total_quantity = defaultdict(int)

    for op in operations:  
        kind = op[0]

        if kind == "stock":
            event, price, quantity = op[1], op[2], op[3]

            if event_to_price_quantity[event].get(price, 0) == 0:
                heapq.heappush(event_to_min_heap[event], price)

            event_to_price_quantity[event][price] = (
                event_to_price_quantity[event].get(price, 0) + quantity
            )
            event_to_total_quantity[event] += quantity

        elif kind == "sell":
            event, quantity = op[1], op[2]

            if event_to_total_quantity[event] < quantity:
                res.append(-1)
                continue

            num_sold = 0
            total_price = 0
            price_map = event_to_price_quantity[event]
            heap = event_to_min_heap[event]

            while num_sold < quantity:
                # lazy deletion of stale heap entries
                while heap and heap[0] not in price_map:
                    heapq.heappop(heap)

                min_price = heapq.heappop(heap)
                min_price_quantity = price_map[min_price]
                amount_to_take = min(min_price_quantity, quantity - num_sold)

                total_price += amount_to_take * min_price
                num_sold += amount_to_take
                event_to_total_quantity[event] -= amount_to_take

                remaining = min_price_quantity - amount_to_take
                if remaining == 0:
                    del price_map[min_price]
                else:
                    price_map[min_price] = remaining
                    heapq.heappush(heap, min_price)

            res.append(total_price)

        elif kind == "reprice":
            event, old_price, new_price, quantity = op[1], op[2], op[3], op[4]

            if old_price == new_price:
                continue

            price_map = event_to_price_quantity[event]
            old_qty = price_map.get(old_price, 0)

            if old_qty < quantity:
                continue

            price_map[old_price] = old_qty - quantity
            if price_map[old_price] == 0:
                del price_map[old_price]

            if price_map.get(new_price, 0) == 0:
                heapq.heappush(event_to_min_heap[event], new_price)

            price_map[new_price] = price_map.get(new_price, 0) + quantity

    return res
