import heapq
import importlib.util
import random
import time
from collections import defaultdict
from pathlib import Path

SOLUTION_PATH = Path(__file__).with_name("q3_compute_market_solution.py")

spec = importlib.util.spec_from_file_location("candidate", SOLUTION_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


# ------------------------------
# Reference implementations
# ------------------------------

def reference_solution(operations):
    """Efficient reference solution used for expected outputs."""
    qty = defaultdict(dict)          # region -> {price: units}
    heaps = defaultdict(list)        # region -> min-heap of prices
    totals = defaultdict(int)        # region -> total units
    ans = []

    def clean(region):
        h = heaps[region]
        q = qty[region]
        while h and h[0] not in q:
            heapq.heappop(h)

    for op in operations:
        kind = op[0]

        if kind == "supply":
            _, region, price, units = op
            if qty[region].get(price, 0) == 0:
                heapq.heappush(heaps[region], price)
            qty[region][price] = qty[region].get(price, 0) + units
            totals[region] += units

        elif kind == "rerate":
            _, region, old_price, new_price, units = op
            if old_price == new_price:
                continue
            old_units = qty[region].get(old_price, 0)
            if old_units < units:
                continue

            remaining = old_units - units
            if remaining == 0:
                del qty[region][old_price]
            else:
                qty[region][old_price] = remaining

            if qty[region].get(new_price, 0) == 0:
                heapq.heappush(heaps[region], new_price)
            qty[region][new_price] = qty[region].get(new_price, 0) + units

        elif kind == "allocate":
            _, region, need = op
            if totals[region] < need:
                ans.append(-1)
                continue

            cost = 0
            totals[region] -= need
            while need > 0:
                clean(region)
                price = heaps[region][0]
                take = min(need, qty[region][price])
                qty[region][price] -= take
                cost += price * take
                need -= take
                if qty[region][price] == 0:
                    del qty[region][price]
                clean(region)

            ans.append(cost)

        else:
            raise ValueError(f"Unknown op: {kind}")

    return ans


def brute_solution(operations):
    """Slow but straightforward validator for small random tests."""
    inv = defaultdict(dict)
    ans = []

    for op in operations:
        kind = op[0]

        if kind == "supply":
            _, region, price, units = op
            inv[region][price] = inv[region].get(price, 0) + units

        elif kind == "rerate":
            _, region, old_price, new_price, units = op
            if old_price == new_price:
                continue
            if inv[region].get(old_price, 0) < units:
                continue
            inv[region][old_price] -= units
            if inv[region][old_price] == 0:
                del inv[region][old_price]
            inv[region][new_price] = inv[region].get(new_price, 0) + units

        elif kind == "allocate":
            _, region, need = op
            total = sum(inv[region].values())
            if total < need:
                ans.append(-1)
                continue

            cost = 0
            for price in sorted(list(inv[region].keys())):
                if need == 0:
                    break
                take = min(need, inv[region][price])
                inv[region][price] -= take
                cost += take * price
                need -= take
                if inv[region][price] == 0:
                    del inv[region][price]

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
        raise AssertionError(f"{name} too slow: {elapsed:.3f}s > {max_seconds:.3f}s")


# ------------------------------
# Fixed edge / tricky tests
# ------------------------------

def fixed_tests():
    cases = []

    cases.append((
        "basic_example",
        [
            ["supply", "us-east", 7, 3],
            ["supply", "us-east", 5, 2],
            ["allocate", "us-east", 4],
            ["rerate", "us-east", 7, 6, 1],
            ["allocate", "us-east", 2],
        ],
        [24, -1],
    ))

    cases.append((
        "independent_regions",
        [
            ["supply", "a", 4, 3],
            ["supply", "b", 2, 5],
            ["allocate", "a", 2],
            ["allocate", "b", 4],
            ["allocate", "a", 2],
        ],
        [8, 8, -1],
    ))

    cases.append((
        "failed_allocate_no_mutation",
        [
            ["supply", "eu", 9, 2],
            ["allocate", "eu", 3],
            ["allocate", "eu", 2],
        ],
        [-1, 18],
    ))

    cases.append((
        "ignore_bad_rerate",
        [
            ["supply", "ap", 11, 2],
            ["rerate", "ap", 11, 8, 3],
            ["allocate", "ap", 2],
        ],
        [22],
    ))

    cases.append((
        "same_price_rerate_is_noop",
        [
            ["supply", "ca", 6, 5],
            ["rerate", "ca", 6, 6, 4],
            ["allocate", "ca", 4],
            ["allocate", "ca", 2],
        ],
        [24, -1],
    ))

    cases.append((
        "rerated_bucket_becomes_cheapest",
        [
            ["supply", "edge", 9, 3],
            ["supply", "edge", 5, 2],
            ["rerate", "edge", 9, 3, 1],
            ["allocate", "edge", 4],
            ["allocate", "edge", 1],
        ],
        [22, 9],
    ))

    cases.append((
        "stale_heap_entries_after_depletion_and_reopen",
        [
            ["supply", "x", 7, 2],
            ["allocate", "x", 2],
            ["supply", "x", 10, 1],
            ["supply", "x", 7, 1],
            ["allocate", "x", 2],
        ],
        [14, 17],
    ))

    cases.append((
        "merge_into_existing_price_bucket",
        [
            ["supply", "merge", 8, 2],
            ["supply", "merge", 5, 3],
            ["rerate", "merge", 8, 5, 1],
            ["allocate", "merge", 4],
            ["allocate", "merge", 2],
        ],
        [20, -1],
    ))

    cases.append((
        "large_numbers",
        [
            ["supply", "big", 10**9, 10**5],
            ["allocate", "big", 10**5],
        ],
        [10**14],
    ))

    cases.append((
        "missing_old_price",
        [
            ["supply", "m", 13, 2],
            ["rerate", "m", 4, 1, 1],
            ["allocate", "m", 1],
        ],
        [13],
    ))

    cases.append((
        "allocate_exact_total",
        [
            ["supply", "z", 3, 1],
            ["supply", "z", 8, 2],
            ["allocate", "z", 3],
            ["allocate", "z", 1],
        ],
        [19, -1],
    ))

    # Verify hard-coded expectations against the reference to avoid bad tests.
    for name, ops, expected in cases:
        ref = reference_solution(ops)
        if ref != expected:
            raise AssertionError(
                f"Internal test script error in {name}: hardcoded expected {expected} != reference {ref}"
            )
        run_case(name, ops, expected)


# ------------------------------
# Randomized correctness tests
# ------------------------------

def random_small_tests(rounds=400, seed=0):
    rng = random.Random(seed)
    regions = ["us", "eu", "ap", "sa"]

    for t in range(rounds):
        ops = []
        num_ops = rng.randint(1, 90)
        for _ in range(num_ops):
            kind = rng.choices(["supply", "allocate", "rerate"], weights=[5, 4, 3])[0]
            region = rng.choice(regions)
            if kind == "supply":
                price = rng.randint(1, 12)
                units = rng.randint(1, 8)
                ops.append([kind, region, price, units])
            elif kind == "allocate":
                units = rng.randint(1, 12)
                ops.append([kind, region, units])
            else:
                old_price = rng.randint(1, 12)
                new_price = rng.randint(1, 12)
                units = rng.randint(1, 8)
                ops.append([kind, region, old_price, new_price, units])

        expected = brute_solution(ops)
        ref = reference_solution(ops)
        if expected != ref:
            raise AssertionError(
                f"Internal test script mismatch on random_small_{t}\nBrute: {expected}\nRef:   {ref}\nOperations: {ops}"
            )
        run_case(f"random_small_{t}", ops, expected)


# ------------------------------
# Performance-oriented tests
# ------------------------------

def performance_tests():
    ops1 = []
    for price in range(1, 5001):
        ops1.append(["supply", "mega", price, 2])
    for price in range(1, 5001, 2):
        ops1.append(["rerate", "mega", price, price + 10000, 1])
    for _ in range(4000):
        ops1.append(["allocate", "mega", 1])
    run_performance_case("perf_dense_single_region", ops1, max_seconds=2.5)

    ops2 = []
    for i in range(20000):
        region = f"r{i % 500}"
        ops2.append(["supply", region, (i % 100) + 1, 1])
    for i in range(10000):
        region = f"r{i % 500}"
        ops2.append(["allocate", region, 1])
    run_performance_case("perf_many_regions", ops2, max_seconds=2.0)

    rng = random.Random(42)
    regions = [f"zone{i}" for i in range(150)]
    ops3 = []
    for _ in range(70000):
        kind = rng.choices(["supply", "allocate", "rerate"], weights=[6, 3, 2])[0]
        region = rng.choice(regions)
        if kind == "supply":
            ops3.append([kind, region, rng.randint(1, 10**6), rng.randint(1, 5)])
        elif kind == "allocate":
            ops3.append([kind, region, rng.randint(1, 5)])
        else:
            ops3.append([
                kind,
                region,
                rng.randint(1, 10**6),
                rng.randint(1, 10**6),
                rng.randint(1, 3),
            ])
    run_performance_case("perf_large_mixed", ops3, max_seconds=4.0)


if __name__ == "__main__":
    if not hasattr(mod, "solution"):
        raise SystemExit("Could not find solution(operations) in q3_compute_market_solution.py")

    try:
        fixed_tests()
        random_small_tests()
        performance_tests()
    except NotImplementedError:
        raise SystemExit("solution() is still a stub. Implement it, then rerun the tests.")

    print("All tests passed.")
