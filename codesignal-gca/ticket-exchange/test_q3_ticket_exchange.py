import heapq
import importlib.util
import random
import time
from collections import defaultdict
from pathlib import Path

SOLUTION_PATH = Path(__file__).with_name("q3_ticket_exchange_solution.py")

spec = importlib.util.spec_from_file_location("candidate", SOLUTION_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


# ------------------------------
# Reference implementations
# ------------------------------

def reference_solution(operations):
    """Efficient reference solution used for expected outputs."""
    qty = defaultdict(lambda: defaultdict(int))
    heaps = defaultdict(list)
    totals = defaultdict(int)
    ans = []

    def clean(event):
        h = heaps[event]
        q = qty[event]
        while h and q[h[0]] == 0:
            heapq.heappop(h)

    for op in operations:
        kind = op[0]
        if kind == "stock":
            _, event, price, amount = op
            if qty[event][price] == 0:
                heapq.heappush(heaps[event], price)
            qty[event][price] += amount
            totals[event] += amount

        elif kind == "reprice":
            _, event, old_price, new_price, amount = op
            if qty[event][old_price] < amount:
                continue
            if old_price == new_price:
                continue

            qty[event][old_price] -= amount
            if qty[event][new_price] == 0:
                heapq.heappush(heaps[event], new_price)
            qty[event][new_price] += amount

        elif kind == "sell":
            _, event, need = op
            if totals[event] < need:
                ans.append(-1)
                continue

            cost = 0
            totals[event] -= need

            while need > 0:
                clean(event)
                price = heaps[event][0]
                take = min(need, qty[event][price])
                qty[event][price] -= take
                cost += price * take
                need -= take
                clean(event)

            ans.append(cost)

        else:
            raise ValueError(f"Unknown op: {kind}")

    return ans


def brute_solution(operations):
    """Slow but straightforward validator for small random tests."""
    inv = defaultdict(lambda: defaultdict(int))
    ans = []

    for op in operations:
        kind = op[0]

        if kind == "stock":
            _, event, price, amount = op
            inv[event][price] += amount

        elif kind == "reprice":
            _, event, old_price, new_price, amount = op
            if inv[event][old_price] >= amount:
                if old_price != new_price:
                    inv[event][old_price] -= amount
                    if inv[event][old_price] == 0:
                        del inv[event][old_price]
                    inv[event][new_price] += amount

        elif kind == "sell":
            _, event, need = op
            total = sum(inv[event].values())
            if total < need:
                ans.append(-1)
                continue

            cost = 0
            for price in sorted(inv[event]):
                if need == 0:
                    break
                take = min(need, inv[event][price])
                inv[event][price] -= take
                cost += take * price
                need -= take

            for p in list(inv[event].keys()):
                if inv[event][p] == 0:
                    del inv[event][p]

            ans.append(cost)

        else:
            raise ValueError(f"Unknown op: {kind}")

    return ans


# ------------------------------
# Helpers
# ------------------------------

def run_case(name, operations, expected=None):
    actual = mod.solution(operations)
    if expected is None:
        expected = reference_solution(operations)
    if actual != expected:
        raise AssertionError(
            f"{name} failed\nExpected: {expected}\nActual:   {actual}\nOperations: {operations}"
        )


def run_performance_case(name, operations, max_seconds):
    start = time.perf_counter()
    actual = mod.solution(operations)
    elapsed = time.perf_counter() - start
    expected = reference_solution(operations)
    if actual != expected:
        raise AssertionError(f"{name} failed correctness during performance test")
    if elapsed > max_seconds:
        raise AssertionError(
            f"{name} too slow: {elapsed:.3f}s > {max_seconds:.3f}s"
        )


# ------------------------------
# Fixed edge / tricky tests
# ------------------------------

def fixed_tests():
    cases = []

    # Basic example
    cases.append((
        "basic_example",
        [
            ["stock", "concert", 50, 4],
            ["stock", "concert", 30, 2],
            ["sell", "concert", 5],
            ["reprice", "concert", 50, 40, 1],
            ["sell", "concert", 2],
        ],
        [210, -1],
    ))

    # Separate event types must not interfere
    cases.append((
        "independent_events",
        [
            ["stock", "concert", 10, 3],
            ["stock", "sports", 5, 4],
            ["sell", "concert", 2],
            ["sell", "sports", 3],
            ["sell", "concert", 2],
        ],
        [20, 15, -1],
    ))

    # Failed sell must not modify inventory
    cases.append((
        "failed_sell_no_mutation",
        [
            ["stock", "expo", 8, 2],
            ["sell", "expo", 3],
            ["sell", "expo", 2],
        ],
        [-1, 16],
    ))

    # Reprice ignored if insufficient quantity
    cases.append((
        "ignore_bad_reprice",
        [
            ["stock", "theater", 20, 2],
            ["reprice", "theater", 20, 15, 3],
            ["sell", "theater", 2],
        ],
        [40],
    ))

    # Reprice to same price is a no-op
    cases.append((
        "same_price_reprice",
        [
            ["stock", "comedy", 12, 5],
            ["reprice", "comedy", 12, 12, 3],
            ["sell", "comedy", 4],
            ["sell", "comedy", 2],
        ],
        [48, -1],
    ))

    # Cheapest-first across multiple buckets after repricing
    cases.append((
        "repriced_bucket_becomes_cheapest",
        [
            ["stock", "opera", 30, 3],
            ["stock", "opera", 20, 2],
            ["reprice", "opera", 30, 10, 1],
            ["sell", "opera", 4],
            ["sell", "opera", 1],
        ],
        [80, 30],
    ))

    # Stale heap entries from full depletion and later restocking
    cases.append((
        "stale_heap_entries",
        [
            ["stock", "festival", 7, 2],
            ["sell", "festival", 2],
            ["stock", "festival", 9, 1],
            ["stock", "festival", 7, 1],
            ["sell", "festival", 2],
        ],
        [14, 16],
    ))

    # Large arithmetic / 64-bit behavior
    cases.append((
        "large_numbers",
        [
            ["stock", "vip", 10**9, 10**5],
            ["sell", "vip", 10**5],
        ],
        [10**14],
    ))

    # Sell exactly total inventory
    cases.append((
        "sell_exact_total",
        [
            ["stock", "indie", 5, 1],
            ["stock", "indie", 8, 2],
            ["sell", "indie", 3],
            ["sell", "indie", 1],
        ],
        [21, -1],
    ))

    # Reprice from missing bucket ignored
    cases.append((
        "missing_old_price",
        [
            ["stock", "edm", 11, 2],
            ["reprice", "edm", 12, 3, 1],
            ["sell", "edm", 1],
        ],
        [11],
    ))

    for name, ops, expected in cases:
        run_case(name, ops, expected)


# ------------------------------
# Randomized correctness tests
# ------------------------------

def random_small_tests(rounds=300, seed=0):
    rng = random.Random(seed)
    events = ["concert", "sports", "opera", "expo"]

    for t in range(rounds):
        ops = []
        num_ops = rng.randint(1, 80)

        for _ in range(num_ops):
            kind = rng.choices(["stock", "sell", "reprice"], weights=[5, 4, 3])[0]
            event = rng.choice(events)

            if kind == "stock":
                price = rng.randint(1, 12)
                qty = rng.randint(1, 8)
                ops.append([kind, event, price, qty])

            elif kind == "sell":
                qty = rng.randint(1, 12)
                ops.append([kind, event, qty])

            else:
                old_price = rng.randint(1, 12)
                new_price = rng.randint(1, 12)
                qty = rng.randint(1, 8)
                ops.append([kind, event, old_price, new_price, qty])

        expected = brute_solution(ops)
        run_case(f"random_small_{t}", ops, expected)


# ------------------------------
# Performance-oriented tests
# ------------------------------

def performance_tests():
    # Many operations concentrated in one event with frequent sells/reprices.
    ops1 = []
    for price in range(1, 5001):
        ops1.append(["stock", "mega", price, 2])
    for price in range(1, 5001, 2):
        ops1.append(["reprice", "mega", price, price + 10000, 1])
    for _ in range(4000):
        ops1.append(["sell", "mega", 1])
    run_performance_case("perf_dense_single_event", ops1, max_seconds=2.5)

    # Many event types to catch poor global scans.
    ops2 = []
    for i in range(20000):
        event = f"e{i % 500}"
        ops2.append(["stock", event, (i % 100) + 1, 1])
    for i in range(10000):
        event = f"e{i % 500}"
        ops2.append(["sell", event, 1])
    run_performance_case("perf_many_event_types", ops2, max_seconds=2.0)

    # Large-ish mixed random scenario.
    rng = random.Random(42)
    events = [f"evt{i}" for i in range(150)]
    ops3 = []
    for _ in range(70000):
        kind = rng.choices(["stock", "sell", "reprice"], weights=[6, 3, 2])[0]
        event = rng.choice(events)

        if kind == "stock":
            ops3.append([kind, event, rng.randint(1, 10**6), rng.randint(1, 5)])
        elif kind == "sell":
            ops3.append([kind, event, rng.randint(1, 5)])
        else:
            ops3.append([
                kind,
                event,
                rng.randint(1, 10**6),
                rng.randint(1, 10**6),
                rng.randint(1, 3),
            ])

    run_performance_case("perf_large_mixed", ops3, max_seconds=4.0)


if __name__ == "__main__":
    if not hasattr(mod, "solution"):
        raise SystemExit(
            "Could not find solution(operations) in q3_ticket_exchange_solution.py"
        )

    try:
        fixed_tests()
        random_small_tests()
        performance_tests()
    except NotImplementedError:
        raise SystemExit("solution() is still a stub. Implement it, then rerun the tests.")

    print("All tests passed.")
