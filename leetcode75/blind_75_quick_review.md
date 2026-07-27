# Blind 75 Quick Review Guide

A concise refresher of the main patterns in the Blind 75.

Focus on recognizing **which pattern applies**, rather than memorizing exact solutions.

---

## 1. Arrays and Hash Maps

Use a `dict` or `set` for fast lookup, counting, or checking duplicates.

### Example: Two Sum

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
```

- **Time:** `O(n)`
- **Space:** `O(n)`

---

## 2. Two Pointers

Use two indices that move through an array, often toward each other.

This is especially common with sorted arrays.

### Example: 3Sum

```python
def three_sum(nums):
    nums.sort()
    result = []

    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = num + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([num, nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return result
```

- **Time:** `O(n²)`
- **Space:** `O(1)` excluding the result

---

## 3. Sliding Window

Use for a continuous section of an array or string.

Expand the right side and shrink the left side when the window becomes invalid.

### Example: Longest Substring Without Repeating Characters

```python
def length_of_longest_substring(s):
    chars = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1

        chars.add(s[right])
        longest = max(longest, right - left + 1)

    return longest
```

- **Time:** `O(n)`
- **Space:** `O(n)`

---

## 4. Stack

Use when the most recently added item must be processed first.

Common uses include matching brackets, parsing expressions, and maintaining monotonic order.

### Example: Valid Parentheses

```python
def is_valid(s):
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    stack = []

    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)

    return not stack
```

- **Time:** `O(n)`
- **Space:** `O(n)`

---

## 5. Binary Search

Use on sorted data when you can eliminate half of the search space each step.

### Example: Search in Rotated Sorted Array

```python
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

- **Time:** `O(log n)`
- **Space:** `O(1)`

---

## 6. Linked Lists

Keep track of node references carefully.

Common techniques include reversing pointers and using slow and fast pointers.

### Example: Reverse Linked List

```python
def reverse_list(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous
```

- **Time:** `O(n)`
- **Space:** `O(1)`

---

## 7. Trees

Use DFS for recursive subtree problems.

Use BFS when processing the tree level by level.

### Example: Maximum Depth of Binary Tree

```python
def max_depth(root):
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)
```

- **Time:** `O(n)`
- **Space:** `O(h)`, where `h` is the tree height

---

## 8. Heaps and Priority Queues

Use when you repeatedly need the smallest or largest item.

Python's `heapq` implements a min heap.

### Example: Kth Largest Element

```python
import heapq


def find_kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
```

Keep only the `k` largest values. The heap root is the kth largest.

- **Time:** `O(n log k)`
- **Space:** `O(k)`

---

## 9. Backtracking

Try a choice, recursively explore it, and then undo the choice.

Think: **choose, explore, undo**.

### Example: Combination Sum

```python
def combination_sum(candidates, target):
    result = []

    def dfs(index, total, path):
        if total == target:
            result.append(path.copy())
            return

        if index == len(candidates) or total > target:
            return

        path.append(candidates[index])
        dfs(index, total + candidates[index], path)
        path.pop()

        dfs(index + 1, total, path)

    dfs(0, 0, [])
    return result
```

- **Time:** Exponential
- **Space:** Depends on recursion depth

---

## 10. Graphs

Use DFS or BFS to explore connected nodes.

Track visited nodes to avoid processing the same node repeatedly.

### Example: Number of Islands

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(row, col):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or grid[row][col] != "1"
        ):
            return

        grid[row][col] = "0"

        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                islands += 1
                dfs(row, col)

    return islands
```

- **Time:** `O(rows × cols)`
- **Space:** `O(rows × cols)` in the worst case

---

## 11. One-Dimensional Dynamic Programming

Store answers to smaller subproblems instead of recalculating them.

Try to define:

1. What does `dp[i]` represent?
2. What previous states does it depend on?
3. What is the base case?

### Example: House Robber

```python
def rob(nums):
    two_back = 0
    one_back = 0

    for money in nums:
        current = max(one_back, two_back + money)
        two_back = one_back
        one_back = current

    return one_back
```

At each house, either skip it or rob it and add the result from two houses ago.

- **Time:** `O(n)`
- **Space:** `O(1)`

---

## 12. Two-Dimensional Dynamic Programming

Use when the state depends on two variables, such as two indices or grid coordinates.

### Example: Unique Paths

```python
def unique_paths(rows, cols):
    dp = [[1] * cols for _ in range(rows)]

    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

    return dp[-1][-1]
```

Each cell can be reached from above or from the left.

- **Time:** `O(rows × cols)`
- **Space:** `O(rows × cols)`

---

## 13. Intervals

Sort intervals by their starting point.

Then compare each interval with the previously merged interval.

### Example: Merge Intervals

```python
def merge(intervals):
    intervals.sort()
    merged = []

    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged
```

- **Time:** `O(n log n)`
- **Space:** `O(n)`

---

## 14. Greedy

Make the best local decision while maintaining an invariant about what remains possible.

### Example: Jump Game

```python
def can_jump(nums):
    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0
```

Move the goal backward whenever a position can reach it.

- **Time:** `O(n)`
- **Space:** `O(1)`

---

## 15. Tries

A trie stores strings character by character.

Use it for prefix searches and dictionary-based word problems.

### Example: Implement Trie

```python
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root

        for char in word:
            node = node.setdefault(char, {})

        node["#"] = True

    def search(self, word):
        node = self.root

        for char in word:
            if char not in node:
                return False

            node = node[char]

        return "#" in node

    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node:
                return False

            node = node[char]

        return True
```

- **Insert:** `O(m)`
- **Search:** `O(m)`
- `m` is the length of the word or prefix

---

## 16. Bit Manipulation

Use binary operators when the problem involves bits, powers of two, or XOR.

Useful operators:

```text
&   AND
|   OR
^   XOR
~   NOT
<<  Left shift
>>  Right shift
```

### Example: Counting Bits

```python
def count_bits(n):
    result = [0] * (n + 1)

    for number in range(1, n + 1):
        result[number] = result[number >> 1] + (number & 1)

    return result
```

Removing the final bit gives a smaller number whose answer is already known.

- **Time:** `O(n)`
- **Space:** `O(n)`

---

# Fastest Review Order

Prioritize these topics in this order:

1. Arrays and hash maps
2. Two pointers and sliding window
3. Trees and graphs
4. One-dimensional dynamic programming
5. Binary search
6. Linked lists and stacks
7. Backtracking
8. Heaps, intervals, and greedy
9. Two-dimensional dynamic programming
10. Tries and bit manipulation

# Suggested Review Method

Solve each example from memory.

For every problem, quickly identify:

- The input and output
- The pattern
- The main data structure
- The time and space complexity
- The important edge cases

Any pattern that takes more than about 20 minutes should become your next review area.
