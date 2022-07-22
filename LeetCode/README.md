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
- [x] 394. Decode String (Medium)
> Given an encoded string, return its decoded string.

```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"
```

_Use stack for an iterative solution. When coming across a `[` character, put a `current` decoded string onto a stack (together with a quantifier preceding given `[`) and start building a new `current` until hitting `]`._