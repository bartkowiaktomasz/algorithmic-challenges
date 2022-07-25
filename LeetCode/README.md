# LeetCode - Other Questions
Solutions to LeetCode problems

---
- [x] 4Sum (Medium)
> Given an array nums of `n` integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
```
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
```
- Solve the general case: `NSum` recursively with 2Sum as base case - complexity `O(N^3)` which is optimal.

---
- [x] 24. Swap Nodes in Pairs (Medium)

> Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

- Use three pointers: `left, a, b` where `a, b` are to be swapped

---
- [x] 25. Reverse Nodes in k-Group (Hard)

> Given the head of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

- Use three pointers: `start, stop, next_` to reverse the linked list between `start, stop` at each iteration. Alternatively, use recursion

---
- [x] 31. Next Permutation (Medium)
> Given an array of integers `nums`, find the next permutation of `nums`. E.g. next permutation of arr = `[1,2,3]` is `[1,3,2]`. For arr = `[2,3,1]` it's `[3,1,2]`

- Scan right-to-left until a number is found such that `nums[i] < nums[i + 1]`. Swap it with the _next smaller_ number to its right. Reverse the suffix `nums[i + 1:]` to get the smallest lexicographically permutation (see a detailed description in the code).

---
- [x] 32. Longest Valid Parentheses (Hard)
> Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

- Use stack for `O(N)`. In the stack, **keep indices** of opening parentheses. Note: Instantiate the `stack` as `stack = [-1]` to deal with e.g. `()()` gracefully (answer: 4). In this example, when coming across the second `)` (index 3) the length is calculated as `l = 3 - (-1) = 4` (Note: we always `pop` the topmost elem in the stack and then compute the current length w.r.t. the new stack top). If we have a `)` but the stack is empty, we push its index onto the stack - this allows us to deal wih e.g. `())()()` gracefully (answer: 4) - last length will be computed as `l = 6 - 2 = 4`

---
- [x] 35. Search Insert Position (Easy)
> Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

- Binary search. `while(l < r)` and always return `l`. 

---
- [x] 39. Combination Sum
> Given an array of distinct integers `candidates` and a `target` integer `target`, return a list of all unique combinations of candidates where the chosen numbers sum to `target`. You may return the combinations in any order.

- Naive recursive solution with recursive relation:
```
for i in range(len(candidates)):
    solve(candidates[i:], [candidates[i]] + cur, target - candidates[i])
```
Remark: Notice `candidates[i:]` which allows for skipping duplicates.

---
- [x] 45. Jump Game II
> Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps.

- DP from backwards. Optimisation: BFS. For each node, find the leftmost one that can reach `destination` in one jump. Mark it as a new `destination`, increment the jump counter and repeat until `destination` is at index 0.

---
- [x] 394. Decode String (Medium)
> Given an encoded string, return its decoded string.

```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"
```

_Use stack for an iterative solution. When coming across a `[` character, put a `current` decoded string onto a stack (together with a quantifier preceding given `[`) and start building a new `current` until hitting `]`._


