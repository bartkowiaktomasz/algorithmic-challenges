# LeetCode - Other Questions
Solutions to LeetCode problems (solution overviewes provided only for Medium and Hard problems)

- [x] 6. Zigzag Conversion (Medium)
> The string `PAYPALISHIRING` is written in a zigzag pattern
on a given number of rows like this:
```
P   A   H   N
A P L S I I G
Y   I   R
```
> And then read line by line: `PAHNAPLSIIGYIR`

> Write the code that will take a string and make this
conversion given a number of rows

- Preallocate `numRows` many empty strings (one for each row) and iterate through characters `c` of the input string `s` appending each `c` to a relevant preallocated string
```
['', '', ''] -> ['P', '', ''] -> ['P', 'A', ''] -> ['P', 'A', 'Y'] -> ['P', 'AP', 'Y'] -> ['PA', 'AP', 'Y'] -> ...
```
---

- [x] 9. Palindrome Number (Easy*)
> Given an integer x, return true if x is a  palindrome, and false otherwise.
Follow-up: Could you solve it without converting the integer to a string?

_Reverse input number (via `rev_x = (rev_x * 10) + (x % 10), x //= 10`) and compare if `x == rev_x`. Optimisation - only reverse `while x > rev_x`._

---
- [x] 12. Integer to Roman (Medium)
> Given an integer, convert it to a roman numeral, e.g. `1994 -> "MCMXCIV"`


---
- [x] 18. 4Sum (Medium)
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
- [x] 27. Remove element (Easy)

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
- [x] 39. Combination Sum (Medium)
> Given an array of distinct integers `candidates` and a `target` integer `target`, return a list of all unique combinations of candidates where the chosen numbers sum to `target`. You may return the combinations in any order.

- Naive recursive solution with recursive relation:
```
for i in range(len(candidates)):
    solve(candidates[i:], [candidates[i]] + cur, target - candidates[i])
```
Remark: Notice `candidates[i:]` which allows for skipping duplicates.

---
- [x] 45. Jump Game II (Medium)
> Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps.

- DP from backwards. Optimisation: BFS. For each node, find the leftmost one that can reach `destination` in one jump. Mark it as a new `destination`, increment the jump counter and repeat until `destination` is at index 0.

---
- [x] 51. N-Queens (Hard)
> Given an integer `n`, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

- Brute force with backtracking. Optimisations: 1. After placing a queen, skip to next row (two queens cannot be placed in the same row)

---
- [x] 64. Minimum Path Sum (Medium)
> Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

- DP. State:
```
# function "solve"
dp[i][j] = grid[i][j] + min(
    solve(i + 1, j), solve(i, j + 1)
)
```

- [x] 67. Add Binary (Easy)
> Given two binary strings `a` and `b`, return their sum as a binary string e.g. `a = "11", b = "1" => "100"`


---
- [x] 71. Simplify Path (Medium)

> Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

_Use `stack`. Split the path with `/` (`path.split("/")`). Iterate through the list and `pop` from the `stack` if encountered `..`._


---
- [x] 72. Edit Distance (Hard)
> Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

- Use DP. `dp[i][j]` keeps the solution to the subproblem for `word1[i:]` and `word2[j:]` (suffixes). DP state will be different depending on whether `word1[i] == word2[j]` or not. Roughly speaking, for each `i, j` we can either replace the character in `word1`, replace the character in `word2` 

---
- [x] 74. Search a 2D matrix
> Write an efficient algorithm that searches for a value target in an `m x n` integer matrix matrix. Each row is sorted left to right and columns - top to bottom

- Start in the top-right corner and move to the left if target is smaller than the current element, else move to the bottom (or return `True` if `target` is found)

---
- [x] 77. Combinations
> Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

- _Use recursion. Given elements `[1, 2, ..., n]` at each call consider two choices: 1. Take first element (`1`) and 2. Do not take that element. Then recurse into `[2, ..., n]` with `k = k -1`_

---
- [x] 80. Remove Duplicates from Sorted Array II
> Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

- Solution: Two pass: 1. Mark all characters for removal (e.g. using `_`), 2. Use two pointers: slow `i` and fast `j` to swap `_` (pointed by `i`) with appropriate character (pointed by `j`)

---
- [x] 92. Reverse Linked List II
> Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

_Solution: One pass scan. See [solution](ReverseLinkedListII.py)_:
```
# The algorithm advances two pointers: first.next and tail.next
#  at each iteration, increasing the reversed region
#  e.g. revert between 2 and 4
#  1 -> 2 -> 3 -> 4 -> 5
#  f    t
#  1 -> 3 -> 2 -> 4 -> 5
#  f         t
#  1 -> 4 -> 3 -> 2 -> 5
#  f              t
```

---
- [x] 96. Unique Binary Search Trees
> Given an integer `n`, return the number of structurally unique BST's (binary search trees) which has exactly `n` nodes of unique values from `1` to `n`.

- Recursive solution: Say `n = 4`. Feasible trees can start with `1` as root, `2` as root, ..., `4` as root. Valid BST trees for a given root will only have nodes `i` such that for the left subtree `i < root` and for the right subtree: `i > root`. 
Remark: The answer is the n'th [Catalan number](https://en.wikipedia.org/wiki/Catalan_number)

---
- [x] 100. Same Tree (Easy)
> Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

---
- [x] 106. Construct Binary Tree from Inorder and Postorder Traversal
> Given two integer arrays `inorder` and `postorder` where `inorder` is the `inorder` traversal of a binary tree and `postorder` is the `postorder` traversal of the same tree, construct and return the binary tree.

_Note that: 1. Last element of `postorder` is the `root`, 2. `inorder` array will look like `[..., root, ...]`. This means that for each element in `preorder` we can recursively (by `pop`ing) build its left and right subtrees if we know the index of `root` element in the `inorder` array._

---
- [x] 114. Flatten Binary Tree to Linked List
> Given the `root` of a binary tree, flatten the tree into a "linked list":
> The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always null.

- Recursive solution. For each `node`, `flatten` its both subtrees and then recombine pointers so that the `root` together with its flattened left subtree and flattened right subtree form a flattened tree.

---
- [x] 133. Clone Graph (Medium)
> Given a reference of a `node` in a connected undirected graph. Return a deep copy (clone) of the graph.

_Solution: DFS - inner function accepts two nodes: original one and it's clone. Keep track of `map: value -> node object` when updating neighbour pointers in clones_

---
- [x] 135. Candy (Hard)
> There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings. You are giving candies to these children subjected to the following requirements:
> - Each child must have at least one candy.
> - Children with a higher rating get more candies than their neighbors.

> Return the minimum number of candies you need to have to distribute the candies to the children.
- Create two arrays: `l, r`. `l (r)` will track the number of candies needed to ensure that a kid with a higher rating than its left (right) neighbour has more candies. The assigned candies will be an elementwise `max` between `l` and `r`.

---
- [x] 142. Linked List Cycle II (Medium)
> Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

- Use Floyd's cycle detection algorithm

---
- [x] 211. Design Add and Search Words Data Structure (Medium)
> Design a data structure that supports adding new words and finding if a string matches any previously added string. `word` may contain dots '.' where dots can be matched with any letter.

_Use Trie_

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

---
- [x] 153. Find Minimum in Rotated Sorted Array (Medium)
> Rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

_Binary search with three pointers: `low, mid, high` with `low` moving `if nums[mid] > nums[0]: low = mid + 1` (note: we're always comparing against the first number in the array `nums[0]`)_

---
- [x] 199. Binary Tree Right Side View (Medium)

> Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

_Do a level-order traversal. In each level, append to `res` the last (rightmost) element of that level_

---
- [x] 209. Minimum Size Subarray Sum
> Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

_Use Sliding Window approach. Expand the window while `sum(window) < target` and shrink it while `sum(window) >= target`_

---
- [x] 221. Maximal Square (Medium)
> Given an `m x n` binary matrix filled with `0`'s and `1`'s, find the largest square containing only `1`'s and return its area.

_Use DP. State: `dp[i][j]` represents the side length of the largest square who's bottom-right corner is `i, j`. `dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])` if `matrix[i][j] == '1'` (else `0`). Optimisation - when doing bottom-up we only need to keep the last row so `dp` is 1D._

---
- [x] 226. Invert Binary Tree (Easy)
> Given the `root` of a binary tree, invert the tree, and return its `root`.

---
- [x] 228. Summary Ranges (Easy)
> Turn `nums = [0,1,2,4,5,7]` to `["0->2","4->5","7"]`

---
- [x] 274. H-Index (Medium)
> Given an array of integers citations where `citations[i]` is the number of citations a researcher received for their ith paper, return the researcher's h-index. The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

- Solution: For `O(N)` use counting sort and compute cumulative sum (reversed). E.g. `citations = [3,0,6,1,5] -> [1,1,0,1,0,1,1] -> [5,4,3,3,2,2,1]`. The meaning of each entry at idx `idx` is "Number of papers with number of citations >= `idx`"

---
- [x] 383. Ransom Note (Easy)
> Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

---
- [x] 392. Is Subsequence (Easy)
> Given two strings `s` and `t``, return `true`` if `s` is a subsequence of `t`, or false otherwise.


---
- [x] 416. Partition Equal Subset Sum (Medium)
> Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

_Knapsack problem. We're trying to find if there is a subset of elements with sum equal to `sum(nums) / 2`. If laying out `nums` as rows and `target / weight` as columns, each row depends only on the previous row, so `dp` table can be a 1D vector._

---
- [x] 437. Path Sum III (Medium)

> Given the `root` of a binary tree and an integer `targetSum`, return the number of paths where the sum of the values along the path equals `targetSum`.

_DFS. Keep a global `cache`, which, at any time (for a given node) maintains (counts of) lengths of all subpaths (that start at a root node) above a given node (this requires subtracting the counts after invoking the recursive calls). If there exists a length `l` (in `cache`) such that:
```
current node's cumulative length from root - `l` == targetSum
```
then we found a valid subpath_

---
- [x] 438. Find All Anagrams in a String (Medium)
> Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

_Use a running `diff Counter` but count downwards (i.e. we've found an anagram iff `len(diff) == 0`)_

---
- [x] 502. IPO (Hard)

> You are given `n` projects where the `i`th project has a pure profit `profits[i]` and a minimum capital of `capital[i]` is needed to start it.
Initially, you have `w` capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
Pick a list of at most `k` distinct projects from given projects to maximize your final capital, and return the final maximized capital.

_Use priority heap. Sort inputs by increasing capital and, at each step, complete a project with with the highest feasible profit_


---
- [x] 530. Minimum Absolute Difference in BST (Easy)
> Given the `root` of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

_Do inorder traversal to produce a sorted list of elements, followed by running delta between two adjacent elements_

---
- [x] 543. Diameter of Binary Tree (Easy)

> Given the `root` of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

---
- [x] 560. Subarray Sum Equals K (Medium)

> _One pass - keep incrementing `res` while computing a running `cumsum`. For a given `cumsum` we need to be able to quickly identify how many previous `cumsums` are such that `previous_cumsum + k == cumsum` (use `Counter`).

---
- [x] 637. Average of Levels in Binary Tree (Easy)
> Given the `root` of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10e-5 of the actual answer will be accepted.

---
- [x] 647. Palindromic Substrings (Medium)

> Given a string `s`, return the number of palindromic substrings in it.

_2D DP using two pointers: `i, j`. State:_
```
dp[i][j] = 
    - True if dp[i + 1][j - 1] and s[i] == s[j] and j - i >= 2
    - True if s[i] == s[j] if j == i + 1
    - else False
```
_Note: In order to calculate `dp` we need to have calculated `dp[i + 1][j - 1]`, so we need to iterate `i` backwards `for i in reversed(range(len(s)))` and `j` forwards: `for j in range(i, len(s))`_

---
- [x] 739. Daily Temperatures (Medium)
> Given an array of integers `temperatures` represents the daily temperatures, return an array answer such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

_Use non-increasing mono queue (stack) storing temperature indices in the `stack`_

---
- [x] 763. Partition Labels
> You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

_Two passes: First, build a mapping from a letter to its last index in `s`. In second pass, make the partitions_

---
- [x] 909. Snakes and Ladders
> Find the least number of moves required to reach the last square in the "snakes and ladders" game

_Use BFS, tracking `min` distance to each square from starting square_

---
- [x] 918. Maximum Sum Circular Subarray
> Given a circular integer array `nums` of lengt`h` n, return the maximum possible sum of a non-empty subarray of nums.

_Use Kadane's algorithm like in Maximum Sum Subarray but also keep track of minimum sum subarray. At the end, the maximum sum is EITHER a 1. contiguous subarray, 2. circular subarray. In the latter case, the max subarray sum is of a form `total_sum - sum(min_sum)` where `total_sum` is a total array sum and `sum(min_sum)` is a minimum sum of a contiguous subarray found during Kadane's scan_

---
- [x] 994. Rotting Oranges
> Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

_Use BFS_

---
- [x] 1143. Longest Common Subsequence

> Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return 0.

_Use DP: compare (growing) prefixes_