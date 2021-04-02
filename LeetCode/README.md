# LeetCode - Top Interview Questions
Solutions to [**LeetCode - Top Interview Questions**](https://leetcode.com/problemset/top-interview-questions/)

- [x] Two Sum (Easy)

---
- [x] Add Two Numbers (Medium)
> You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 
0 itself.

> e.g. `l1 = 2 -> 4 -> 3`, `l2 = 5 -> 6 -> 4` gives `7 -> 0 -> 8`

_Iterate through both linked lists simultaneously while any of them is non-empty.
Add digits and carry a "carry" to the next operation in case of overflow_

---
- [x] Longest Substring Without Repeating Characters (Medium)
> Given a string `s`, find the length of the longest substring without repeating 
characters. Examples:
```
"abcabcbb" -> 3
"bbbbb" -> 1
"pwwkew" -> 3
"abba" -> 2
```

_TLDR: Keep two pointers `i, j` (`j >= i`) of the longest "unique" substring 
ending in `j`._

_Iterate through each char in `s` keeping a map `char -> idx` to be able to discover a 
duplicate (and its index). If came across a duplicate, update the map with its `idx`. 
Keep track of two indices: `i, j` (`j >= i`) that note the beginning and end of the 
"unique" string ending in `j`._

_If a new `char` does not exist in the map, move `j`_

_If a new `char` exists in the map, move `i` to the right of the existing duplicate
and calculate the length of the substring starting in `i` ending in `j`. Keep track
of the running `max` of the longest substring._

---
- [x] Median of Two Sorted Arrays (Hard)
> Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, 
return the median of the two sorted arrays.

_This can be done in O(min(logm, logn)). Note that median is the number that
cuts given list in half. First, you need to find a partition in a 
smaller list, where a partition is a cut that divides the list into two sublists. For
a given partition we find a corresponding partition for the second list such that the 
number of elements in the left sublists `|LHS|` >= `|RHS|`. We know that the median
is somewhere among the four boundary elements if a partition is a correct partition.
The partition is correct iff max element of the LHS subarray is smaller (or equal) to 
the min element of the RHS subarray (of the other list), e.g. the partitions below are 
correct because `5 < 6` and no element is smaller than `7`_
```
[1, 2, 5, | 7]
[| 6, 8
```
_NOTE: `|` indicates a partition. Finally, if the number of all elements is odd, return
max element on the LHS (cause it's bigger), otherwise take an average of max LHS elem and
min RHS elem._

---
- [x] Longest Palindromic Substring (Medium)
> Given a string `s`, return the longest palindromic substring in `s`.

`O(n^3)`: _Naive implementation. For each substring `O(n^2)` `bool: is_palindrome(s)` 
costs `O(n)`_

`O(n^2 logn)`: 
_Do a binary search over lengths of palindrome. For a given length,
finding a palindrome is `O(n^2)` so with binary search we improve to `O(n^2 logn)`._

_NOTE: In general it might be a good idea to do a BS over possible answers_

 `O(n^2)` (this solution):
_For each character in `s` at index `i` expand outwards comparing letters at indices
`i - d` and `i + d` saving biggest encountered palindrome. Note the second case where
the palindrome has even length so we need to compare letters at indices `i - d , i+1 - d`_

`O(n)`:
_See Manacher's algorithm_

---
- [x] Reverse Integer (Easy)
> Given a 32-bit signed integer, reverse digits of an integer.
If a number overflows, return `0`

_Keep updating `result` with_
```
result = digit + result * 10
```
_Note that if `result == (MAXINT // 10)` the overflow will
happen if `digit > 7`, because `7` is the last number of `2^31` -1
(Multiples of `2` end with (2, 4, 8, 6)... )_

---
- [x] String to Integer (Medium)

_Note: Annoying edge cases like `input="++1"`_

---
- [x] Regular Expression Matching (Hard)

> Given an input string `s` and a pattern `p`, implement regular expression matching 
with support for `.` and `*` where: 

>`.` Matches any single character.

>`*` Matches zero or more of the preceding element.

> The matching should cover the entire input string (not partial).

_Use DP (bottom-up): Set up a boolean matrix of size `S x P` where `S` is the size of 
a string and `P` is a size of a prefix. DP is useful because of the `*` (wildcard) case
where we need to reuse previous (memoized matches), e.g._
```
s = "x", p="xy*" <==> s = "x", p="x"
```
_i.e. `x` matches `xy*` if `x` matches the subpattern `x` (after removing `y*`). Or:_
```
s = "xyy", p="xy*" <==> s = "xy", p="xy*"
```
_i.e. `xyy` matches `xy*` if, when we remove `y`, the resulting `xy` also matches `xy*`._
_As a result, if the char is `*` the result `dp[i][j]` will match if one of the above
cases happens_

_NOTE: For each `dp[i][j]` we're deciding if substring `s[:i]` matches subpattern
`p[:j]`. Also note that we need to initialise the first row of the matrix (empty string)
and the first column (empty pattern)._

---
- [x] Container With Most Water (Medium)
> Given `n` non-negative integers `a1, a2, ..., an`, where each represents a point at 
> coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of 
> the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the
> x-axis forms a container, such that the container contains the most water.

_O(n): (greedy) Use two pointers `i`, `j` that start at edges and get closer to each
other until they are equal. Increment `i` (or decrement `j`) whichever pointer points 
to the smaller line._

_Intuition: Assume there exists some biggest area between indices `a` and `b` (`b > a`).
 Let's try to prove that always moving the pointer that points to the smaller height 
 will eventually find our maximum area. Since we increment pointer `i` 
 (or decrement pointer `j`) either `i` will hit `a` first or `j` will hit 
 `b`. We now need to guarantee that, if `i` hits `a` first, it will stay there until `j`
 hits `b` (or if `j` hits `b` first, it will stay there until `i` hits `a`). 
 Say `i` hits `a` first - since we only decrement `j` if `height[j] < height[i]` we must
 reach `b` eventually - it is impossible for us to find a line higher than `height[i]`
 before reaching `b` because this would mean that the new area is bigger than the one
 between `a` and `b`, which is a contradiction._


---
- [x] Roman to Integer (Easy)

---
- [x] Longest Common Prefix (Easy)
> Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string `""`.

_Every approach needs to scan all characters in all strings so Best Conceivable Runtime
(BCR) is `O(S)` where `S` is the sum of lengths of all strings_

---
- [x] 3Sum (Medium)
> Given an array nums of n integers, are there elements a, b, c in nums such that 
`a + b + c = 0`? Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

_Slow `O(n^2)`: Insert each `e`lement into a hash map and then check, for each element,
if `-(a[i] + a[j])` is in the map_

_`O(n^2)`: Sort an array in `O(nlog)` (Note that you can solve 2Sum in `O(n)` so sorting
is not needed there) and then, for each element `e` in the sorted array, keep two pointers
`i`, `j` (`i` to the right of `e` and `j` at the end of the array) and 
increment/decrement the pointers depending on whether `sum > 0` or not._

_Optimisations: #1: If `nums[i] == nums[i - 1]` then we're gonna find the same `l, r` and 
since we don't want to return duplicates, we can `continue`. #2: If `e > 0` then the sum
with `l` and `r` will be `>0` (array is sorted) so we can `break`._

---
- [x] Letter Combinations of a Phone Number (Medium)
> Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order. A mapping
of digit to letters (just like on the telephone buttons) is given below. Note that `1` 
does not map to any letters.

> e.g. `2 -> "abc", 3-> "def"` etc.

_Solve recursively by stripping `digits` (e.g. `234` -> `23` -> `2`) from the end 
until one digit is left, then return a list of characters mapped to that
digit. Merge this recursively with each letter corresponding to a current digit_  

---
- [x] Remove Nth Node From End of List (Medium)
> Given the head of a linked list, remove the nth node from the end of the list and
return its head. Follow up: Could you do this in one pass?

_Scan the list with two pointers `i, j` with `j` being `n` nodes behind the `i`. In 
this way, when `i` hits the end, we know that the node at `j` needs to be removed_  

---
- [x] Valid Parentheses (Easy)
> Given a string s containing just the characters `'(', ')', '{', '}', '[', ']'`, 
determine if the input string is valid.

_Use stack to solve in `O(n)`. Optimisation: if input string has an odd length, 
return `False`_

---
- [x] Merge Two Sorted Lists (Easy)
> Merge two sorted linked lists and return it as a new sorted list. The new list should 
be made by splicing together the nodes of the first two lists.

---
- [x] Generate Parentheses (Medium)
> Given `n` pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

_Solve recursively. Start with empty string and, for each call, consider adding `(` and
`)` at the end. Base cases should check if parentheses are valid, i.e. if, at any point,
the number of `)` is `>` than the number of `(`. Keep track of the number of `(` and `)`
used so far (e.g. `left`, `right`), once `left == right == n` we know it's a valid 
parentheses so we can append to the solution_

_Remark: The number of well-formed parentheses for `n` pairs of parentheses is `n`th
Catalan Number so the solution scales with `O(4^n/n^(3/2))`_
  
---
- [x] Merge k Sorted Lists (Hard)
> You are given an array of `k` linked-lists lists, each linked-list is sorted in
ascending order. Merge all the linked-lists into one sorted linked-list and return it.

_Iterate each linked list simultaneously, adding new nodes to a priority queue. In
each iteration, `heappop` smallest node in the heap, access its `next` element and add
it to the heap if it exists, otherwise add `inf`. `break` if the smallest element in
the heap is `inf`_

---
- [x] Remove Duplicates from Sorted Array (Easy)
> Given a sorted array `nums`, remove the duplicates in-place such that each element 
appears only once and return the new length

_Remove elements `while` iterating through the array_ 

---
- [x] Implement strStr() (Easy)
> Return the index of the first occurrence of needle in haystack, or `-1` if needle 
is not part of haystack.

_Do a Naive Search in `O(|s||p|)`, Knuth-Morris-Pratt in `O(|s| + |p|)` or Karp-Rabin
in expected `O(|s|)` (or worst-case `O(|s||p|)`). See [Algorithms](https://github.com/bartkowiaktomasz/algorithms)_

---
- [x] Divide Two Integers (Medium)
> Given two integers `dividend` and `divisor`, divide two integers without using 
multiplication, division, and mod operator.

_We use the fact that `divisor << i` is the same as `divisor * 2^i`. Build two `while` 
loops. The inner loop finds the maximum `i` for which we can subtract `divisor * 2^i` 
from `dividend` and still have a non-negative number. In outer loop keep decrementing 
`divisor * 2^i` from `divident` for each `i` we found in the inner loop until we get 
`i == 0`. We also update the answer `res` in the outer loop based on the `i`s. 
For example, for a division `22/3` we're gonna find `i = [2, 1, 0]`
so we're gonna make subtractions `22 - 12 - 6 - 3 = 1` and our result will be updated as 
`res = 2^2 + 2^1 + 2^0 = 4 + 2 + 1 = 7`_


---
- [x] Search in Rotated Sorted Array (Medium)
> You are given an integer array `nums` sorted in ascending order (with distinct values),
and an integer target.
Suppose that `nums` is rotated at some pivot unknown to you beforehand 
(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).
> If target is found in the array return its index, otherwise, return `-1`

_First, find the index of the pivot and then decide, whether to do a binary search
in the left or right sublist. Here pivot is defined as the first value of the 
increasing subsequence which is smaller than the value on its left._


---
- [x] Find First and Last Position of Element in Sorted Array (Medium)
> Given an array of integers nums sorted in ascending order, find the starting 
and ending position of a given target value.
> If target is not found in the array, return `[-1, -1]`.

_Implement two functions: `binary_search_leftmost` and `binary_search_rightmost` and
then combine their outputs to give the starting and ending position of a target value_


---
- [x] Valid Sudoku (Medium)
> Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:
Each row must contain the digits 1-9 without repetition. Each column must contain the 
digits 1-9 without repetition. Each of the nine 3 x 3 sub-boxes of the grid must 
contain the digits 1-9 without repetition.

_Initialise one set per each row, each column and each box (3 * 9 = 27 sets). Then iterate
through the board once, checking for each element if it exists already in one of the
sets (is so - return `False`). Each element at index `i, j` belongs to a box with index
`3 * (i // 3) + (j // 3)`_


---
- [x] First Missing Positive (Hard)
> Given an unsorted integer array `nums`, find the smallest missing positive integer.

_Solve in `O(n)` with `O(1)` extra space. `O(1)` suggests that we need to somehow alter the
original array to mark which positive integers are there or not. Few observations:_
- First missing positive integer in the array of length `l` must be in range `[1, l + 1]`
  e.g. for list `[1, 2, 3]` the first missing positive is `l + 1 = 4`
- We will be marking positive numbers present in the array by multiplying the elements
  at their corresponding indices by `-1`, e.g. if `3` is present in the array - mark 
  `arr[2]` as negative (the index `2` results from the fact that we're indexing from `0`)
- Even though the original array can contain negative numbers we can convert them to
  any positive number `> n` (e.g. `n + 1`) and ignore when scanning because we know that
  they won't be the answer (see p.1). After all, we ignore any element `e` such that
  `e > n or e <= 0`


---
- [x] Count and Say (Easy)
> The count-and-say sequence is a sequence of digit strings defined by the recursive 
formula:
- `countAndSay(1) = "1"`
- `countAndSay(n)` is the way you would "say" the digit string from 
`countAndSay(n-1)`, which is then converted into a different digit string.

_Use Python's `itertools.groupby` to groupby string into list when the key value changes
and then iteratively compute `countAndSay(n+1)` given `countAndSay(n)`_
```pytho
print ["".join(grp) for num, grp in groupby('111234')]
# ['111', '2', '3', '4']
```

---
- [x] Trapping Rain Water (Hard)
> Given `n` non-negative integers representing an elevation map where the width of each 
bar is `1`, compute how much water it can trap after raining.

_`O(N)` solution using stack. Stack keeps track of **indices** of bars. We will add a 
bar to the stack if it's smaller or equal to the top element on the stack (otherwise we will start 
popping elements and updating volume/area). Otherwise we pop bars until we encounter
bigger (or equal) element and update the total area/volume for each popped bar. Note:_
- The reason for appending to stack bars smaller **or equal** is the fact that
once we encounter a bigger bar we will ignore the plateaus of bars with the same
heights and only add one big area at the end. E.g. say the heights are `[2, 1, 1, 1]`
  and we encounter `h = 4`. We will now start popping `1`s, adding the area of 
  `A = w * h = (current_idx - popped_idx - 1) * (min(1, 4) - 1) = 0` each time until we hit
  `2` where we add `A = w * h = (4 - 0 - 1) * (min(4, 2) - 1) = 3 * 1 = 3`.
  
- Note: Each time when we compute the area, the width is the difference between the 
  indices (minus 1) and the height is a difference between the `min(border heights)` and
  the popped bar

- Note: See [Solution using 2 pointers](https://leetcode.com/problems/trapping-rain-water/solution/) on LeetCode

---
- [x] Wildcard Matching (Hard)
> Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching
with support for '`?`' and '`*`' where:
- '`?`' Matches any single character.
- '`*`' Matches any sequence of characters (including the empty sequence).

_Solution using bottom-down DP. Initialise `memo` table of size `|s| + 1 * |p| + 1|` 
to account for memo values for edge cases (empty string/empty pattern). 
Set boundary conditions: `memo[0][0] = True`, `memo[col = 0] = False` (empty pattern),
and for `memo[row = 0]` depending on the character and the previous `memo` value for
that row. Then, for any cell `i, j` assign the boolean value depending on previously 
computed, neighbouring cells:_
- If pattern is `*` we assign `True` if any of `memo[i - 1][j - 1] or memo[i - 1][j] or memo[i][j - 1]`
is true (first case - `*` matches character directly, second case - we skip char but not `*` since `*` matches any sequence,
  third case - we skip `*` because it matches empty sequence)
- If pattern is `?` we can only apply first case - skip char and pattern
- Else the character needs to match the pattern - first case (diagonal)

---
- [x] Permutate (Medium)
> Given an array `nums` of distinct integers, return all the possible permutations.
You can return the answer in any order.

_Recursive solution where base case appends a single result `single_res` to a 
shared `res` list containing all the results. Each call to `permuteRec` makes
`n` new recursive calls for each number (`num`) in `nums`, after appending `num` 
to `single_res` and passing `nums \{num}` (`nums` with removed `num`) to `permuteRec`. This happens until `nums` has only one element, which is a base
case._ 

---
- [x] Rotate Image (Medium)
> You are given an `n x n` 2D matrix representing an image, rotate the image by 90 
degrees (clockwise).
> You have to rotate the image in-place, which means you have to modify the input 
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

_Rotation by 90 degrees is equivalent to matrix transpose + reflection about 
the y-axis. Swap each pair of cells in-place using XOR trick_
```
x = 10
y = 5
x = x ^ y
y = y ^ x
x = x ^ y
# x = 5, y = 10
```

---
- [x] Group Anagrams (Medium)
> Given an array of strings `strs`, group the anagrams together. You can return 
the answer in any order.

_Since the alphabet has 26 characters, use counting sort to check for anagrams. Build a map `count -> list(words)` where `counts` is a count tuple, e.g. `counts('abb') = (1, 2, 0, ..., 0)`._

- [x] Pow (Medium)
> Implement `pow(x, n)`, which calculates `x` raised to the power `n`

_Use DP. Calculate recursively by splitting power `n` into `n // 2` and `n - n // 2` and memoize intermediate solutions to subproblems._

---
- [x] Maximum Subarray (Easy)
> Given an integer array `nums`, find the contiguous subarray (containing at 
least one number) which has the largest sum and return its sum.

_Do linear scan in `O(N)`. For each number consider whether it should be a) added
to a current (running) subarray, b) ignored or c) made a beggining of new running
subarray. We want to add it (a) if a running sum is positive (or equal to 0) and
`n` does not decrease it below 0. We ignore it (b) if it decreases running sum 
from positive to below 0. To decide whether we start new subarray at `n` (c) 
we need to consider two separate cases - whether `n` is contiguous with current
subarray or not (see code). Note: the code also keeps track of indices of the
array that produces max sum._

---
- [x] Spiral Matrix (Medium)
> Given an `m x n` matrix, return all elements of the matrix in spiral order.

_Keep decrementing one of four boundaries after changing direction. Direction
(e.g. `(0,1)` indicating direction to the right) changes after hitting a 
boundary. While moving through the matrix append the cells to a `res` array.
`break` when `len(res) == len(matrix) * len(matrix[0])` (we've seen all cells)._

---
- [x] Jump Game (Medium)
> Given an array of non-negative integers `nums`, you are initially positioned at
 the first index of the array. Each element in the array represents your 
 maximum jump length at that position. Determine if you are able to reach the 
 last index.

_Use DP starting from the end of the array. Trick: When we are at index `i` with
a jump size of `n` **do not** iterate through all elems at indices 
`i + 1, ... i + n` looking if any of the positions is *good*. Instead,
 keep track of one value *lestmost_good* which tracks the leftmost index 
 for which we are in good position. Each position `i` iff 
 `i + nums[i] >= leftmost_good >= i` i.e. `leftmost_good` is within our jump._

---
- [x] Merge Intervals (Medium)
> Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.

e.g.
```
merge([[1,3],[2,6],[8,10],[15,18]]) = [[1,6],[8,10],[15,18]]
merge([[1,4],[4,5]]) = [[1,5]]
```

_Sort by start of intervals. Then solve by linear scan. Note: Remember about a
case where one interval is inside the previous one, e.g. `[[1, 5], [2, 4]...]`
(e.g. skip a loop, i.e. `continue`)._

---
- [x] Unique Paths (Medium)
> A robot is located at the top-left corner of a `m x n` grid.
The robot can only move either down or right at any point in time. The robot is trying to reach the
bottom-right corner of the grid. How many possible unique paths are there?

_Use DP (bottom-up) starting from finish cell and iterating back to the first
cell. The number in a cell indicates the number of ways to get to the finish.
`dp[-1][-1]` (finish) gets a value of 1. State: 
`dp[row][col] = dp[row][col + 1] + dp[row + 1][col]` (i.e. move to the right 
and down respectively)._

---
- [x] Plus One (Easy)
> Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.


---
- [x] Sqrt(x) (Easy)
> Given a non-negative integer `x`, compute and return the square root of `x`.

_Do binary search over the answers. Improvement: use Newton's method 
with initial guess being `x`_

---
- [x] Climbing Stairs (Easy)
> You are climbing a staircase. It takes n steps to reach the top. 
Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

---
- [x] Set Matrix Zeros (Medium)
> Given an `m x n matrix. If an element is `0`, set its entire row and column to `0`.
 Do it in-place.

_Use first row and first column to mark (with zero) whether it should be 
set to zero. But before doing the full scan, scan the first row and first columns
to decide whether they should be converted to zero as well or not (use two 
boolean variables. Then perform matrix scan, marking which rows/columns contain
zeros. Then, scan through the first row and column and overwrite matrix in place.
At the end, set first row or column to zero based on the boolean values calculated
at the beginning._

---
- [x] Sort Colors (Medium)
> Given an array nums with `n` objects colored red, white, or blue, sort them 
in-place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue. We will use the integers `0, 1`, and `2` to represent
the color red, white, and blue, respectively.

_Use three pointers: `left, mid, right` and swap elements until `mid <= right`. 
Swap according to the color encountered by `mid` - moving `0`s to the left by 
swapping with `left`, leaving `1`s in their place and moving `2`s to the 
right by swapping with `right`._ 

---
- [x] Minimum Window Substring (Hard)
> Given two strings `s` and `t`, return the minimum window in `s` which will 
contain all the characters in `t`. If there is no such window in `s` that covers 
all characters in `t`, return the empty string `""`. Note: `t` can contain
duplicates and the output window needs to contain all of them.

_Linear scan with two pointers: `low, high`. Increment `high` in outer `while`
loop as long as `high < len(s)`. Whenever we have a window between `low` and `high`
such that `s[low:high + 1]` contains all the required chars in `t`, start
shrinking the window by incrementing `low` as long as the window contains 
all elements from `t` (use `Counter` to keep track of those counts)._

---
- [x] Subsets (Medium)
> Given an integer array nums of unique elements, return all possible subsets 
(the power set).

_Solve recursively, at each step branching into two subproblems, one which takes the leftmost element of `nums` into the result, and the other one rejecting the leftmost and considering only `nums[1:]` elements._

---
- [x] Word Search (Medium)
> Given an `m x n` board and a word, find if the word exists in the grid.

_Solve recursively using DFS, keeping track of `visited` cells in a current DFS path, otherwise we would allow for going to the cell we came from._


--- 
- [x] Largest Rectangle in Histogram (Hard)
> Given `n` non-negative integers representing the histogram's bar height where 
the width of each bar is 1, find the area of largest rectangle in the histogram.

_Use stack of bar indices (heights can be looked up quickly given an index). The rep invariant in the stack is that, for a given bar, the bar to its left is necessarily smaller, so we only insert bars that are higher than the `top`. If we come across a bar that's smaller than `top` we pop the stack and calculate the area for each of the popped bars. The height of the area is the height of the popped bar. Insert dummy bar with `height = 0` at the end of the list to deal with an edge case._

---
- [x] Merge Sorted Array (Easy)
> Given two sorted integer arrays `nums1` and `nums2`, merge `nums2` into `nums1` as one sorted array (in place).
> e.g. 
```
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

# result: [1,2,2,3,5,6]
```
_Start filling `nums1` from the end instead of from the beginning. Keep three pointers: `i` (`j`) to iterate through `nums1` (`nums2`) and `k` to keep track where to insert an element (larger of the ones pointed to by `i,j`) into `nums1`. We're done when either of `i, j` arrived at `-1`._

---
- [x] Decode Ways (Medium)
> Given a string `s` containing only digits, return the number of ways to decode it. e.g. `"11106"` can be decoded into `AAJF` `(1 1 10 6)` and
`KJF` `(11 10 6)`. The mapping is `'A' -> '1', ... 'Z' -> '26'` etc

_Use DP (top-down) with 1D memo table of size `len(s) + 1`. `dp[0] = 1` because once we've scanned the entire string we've discovered one way to decode a string. Otherwise the dp state is `dp[i] = dp[i - 1] + dp[i - 2]` assuming if it is possible to decode `s[1:]` and `s[2:]` respectively (e.g. there is no way to decode `"06"`)._

---
- [x] Binary Tree Inorder Traversal (Medium)
> Given the `root` of a binary tree, return the inorder traversal of its 
nodes' values.

_Use `stack` and two `while` loops to solve iteratively. Initialise stack with single `None` element to exit gracefully from the outer `while` loop  (we exit when `stack` is empty and `root is None`, i.e we retrieved first, initial element form the stack)._

_See [How to solve Tree questions using iterative in-order traversal](https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution))_


---
- [x] Validate Binary Search Tree (Medium)
> Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

_Iterative solution using `stack`. Keep track of `previous` node to compare it with `root` each time after retrieving it from the stack. If `previous.val >= root.val` at any time, the BST is invalid (Note the task imposes a constraint that BST keys (of children) must be strictly less or greater than the parent_.
 
 ---
 - [x] Symmetric Tree (Easy)
 > Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

_In the iterative approach use one queue and, while it's not empty, retrieve two nodes at a time, compare them and then add their four children to the queue._

---
- [x] Binary Tree Level Order Traversal (Medium)
> Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

_Use two queues (one - temporary). The first queue keeps all nodes at height `n`. Then, we pop all of the nodes from the queue and add its children to a temporary second queue until we've popped all the elements from the first queue. Then we swap the queues. The algorithm returns when no children are added to a queue_

---
- [x] Binary Tree Zigzag Level Order Traversal (Medium)
> Given the `root` of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

_Reuse previous solution with stacks and add an additional variable `direction` which switches between `1 <-> -1` at each height and decides in which order to insert children to the stack._

---
- [x] Maximum Depth of Binary Tree (Easy)
> Given the `root` of a binary tree, return its maximum depth.

---
- [x] Construct Binary Tree from Preorder and Inorder Traversal (Medium)
> Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

_Note that: 1. First element of `preorder` is the `root`, 2. `inorder` the array will look like `[..., root, ...]`. This means that for each element in `preorder` we can recursively build its left and right subtrees if we know the index of `root` element in the `inorder` array._

---
- [x] Convert Sorted Array to Binary Search Tree (Easy)
> Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

_For an iterative solution use stack, where each element is a `(node, left, right)` tuple. Node in the stack does not have a value assigned yet, it gets assigned a value `nums[(l + r) // 2]` after popping. Then, the range `[l ,r]` is further divided into two subsets (excluding `mid`), and corresponding children nodes are created. When `l == r` we don't need to create any new children, and when `r == l + 1` this means that we need to create a node for `nums[r]` which is a right child for `nums[l]` which had already been._


---
- [x] Populating Next Right Pointers in Each Node (Medium)
> Populate each `next` pointer to point to its next right node. If there is no next right node, the `next` pointer should be set to NULL.

_Iterate over levels starting from root and going down. For each level `i` populate the attribute `next` of each node in the level below (`i+1`) (otherwise we don't have parent pointers on our disposal) starting from the leftmost node and going to the right inside the inner `while` loop (we're going to the right with `tmp = tmp.next`)._

---
- [x] Pascal's Triangle (Easy)

> Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

_Use DP - build `i`th row using `i-1`th row. Note: `i`th row can also be constructed from adding `i-1`th row to itself after shifting numbers by 1 to the right, e.g. for row `1 2 1` the next row will be_
```
1 2 1
  1 2 1
-------
1 3 3 1
```

---
- [x] Best Time to Buy and Sell Stock (Easy)
> You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

_Note: Can use stack_


---
- [x] Best Time to Buy and Sell Stock II (Easy)
> You are given an array `prices` for which the `i`th element is the price of a given stock on day `i`. Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

_Note: Highest profit can be achieved by selling immediately when the price is higher than the previous price, e.g. if prices are_
```
[1, 2, 3]
```
_We should buy for 1$, sell for 2$ (1$ profit), buy for 2$ and sell for 3$ (1$ more profit), getting a total profit of 2$ (as if we did not do any transaction at 2$ price)._


---
- [x] Binary Tree Maximum Path Sum (Hard)
> Given the `root` of a binary tree, return the maximum path sum of any path.

_Note: the question is about a maximum path sum and not a maximum subtree sum. Do a postorder traversal (first - leaves, root at the end), calculating a `max_path_sum` for each node, where `max_path_sum` is the maximum path sum at a given node (maximum of its own sum or it's sum plus either of its children but not both). For each node in the higher levels of the tree we recompute `max_path_sum` using `max_path_sum` of its children. Note that the maximum path might be a one that includes all: some node `n` and `n.left` and `n.right`, but then it cannot include `n.parent` because it would no longer be a path. So the final result will not be a max of `max_path_sum` - we also need to, at each step, compute a value of `n.val + n.left.max_path_sum + n.right.max_path_sum` and update our `max_sum` if necessary. `max_sum` is the final result._

---
- [x] Valid Palindrome (Easy)
> Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

_Watch out for inputs such as `".,"` (True), `"  "` (True)_

---
- [x] Word Ladder (Hard)
> Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

e.g.
```
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# result: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")
```

_Solve using bidirectional BFS. Two words are neighbours in a graph iff you can change one letter in one to get the other. Instead of using queue in BFS use `set`s (one per direction) to track currently considered nodes and a set `visited` to keep track of which nodes have been visited_

---
- [x] Longest Consecutive Sequence (Hard)
> Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

e.g.
```
nums = [100,4,200,1,3,2]
# result: 4 (The longest consecutive elements sequence is [1, 2, 3, 4]

nums = [0,3,7,2,5,8,4,6,0,1]
# result: 9
```

_Linear scan + hashmap. First, add all elements to a hashmap (key - element, value - length of consecutive sequence (lcs) starting at that element). For each element of the list, do an inner loop to check if conecutive elements are in the map and then backtrack, updating the lcs for each backtracked element. So for e.g. `[2, 3, 4, 1]` when we hit `1` the hashmap for element `2` will have had the value of `3` (the lcs for that element is `3`)._ 


---
- [x] Surrounded Regions (Medium)
> Given an `m x n` matrix board containing `'X'` and `'O'`, capture all regions surrounded by `'X'`. A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region. `'O'` is captured if it's not at the boundary or connected to the boundary by other `'O'`s

_BFS with `set` as a queue, searching from all `O`s at the borders of the `board`. Any 'O` reachable form `O` at the border will not be captured - mark that cell with `K` (keep). After BFS, capture all `O` cells which haven't been changed to `K`._

---
- [x] Palindrome Paritioning (Medium)
> Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`. A palindrome string is a string that reads the same backward as forward.

e.g.
```
s = "aab"
# result: [["a","a","b"],["aa","b"]]
```

_DP recursive solution, where `dp[i][j]` denotes whether the string `s` between the indices `i, j` (inclusive) is a palindrome. Start with two pointers `i, j = 0, 0` and recursively search for solutions by moving `i, j` through the string. At each step we call recursively for `i + 1, j + 1` and/or `i, j + 1` and append a single result to a global `res` if we hit a boundary condition._

---
- [x] Gas Station (Medium)

> Given two integer arrays `gas` (The amount of gas available at each gas station) and `cost` (the consumption of gas), return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is guaranteed to be unique. 

e.g.
```
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# result: 3 (you can start at gas station at index 3 and do a round trip)
```
_Insight: Compute `delta = gas - cost`. If `sum(delta) >= 0` there always exists a solution, otherwise return `-1`. Then, compute a `cumsum(delta)` - the starting index (result) is `idx + 1` where `idx` is the lowest `cumsum` value. Proof: if `cumsum(delta)` is the lowest for `idx`, then driving from `0,...,idx` gives us the lowest (negative) value of gas (say `-max`). This means that driving from `idx + 1, ..., n - 1` must give us at least `max` (since `sum(delta) >= 0`) which is then sufficient to cover the entire distance `0, ..., idx`. If driving from `idx + 1, ..., n-1` leaves us at some point with negative gas, then this must mean that `idx` wasn't the lowest cumulative sum to begin with._

---
- [x] Single Number (Easy)
> Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

_XOR all of the numbers with `0`. Only those bits corresponding to numbers that appeared odd number of times will remain._

---
- [x] Copy List with Radom Pointer (Medium)
> Make a copy of a linked list. Any node in the list has a pointer `node.random` which points to a random node in the list

_Do three passes with `O(1)` space (apart from copied list). Start with a list e.g. `2 -> 4 -> 1`. In the first pass make copies of each node and build a one long linked list, i.e. `2 -> 2' -> 4 -> 4' -> 1 -> 1'`. In the second pass assign the random pointers of the copied nodes using the fact that the random pointer of a copied node will point to the `next` element of the random pointer pointed by its predecessor (original node). So if `4.random -> 1` then we have `4'.random -> 4.random.next`. In the third pass take every other node from the long list (`head_cp.next = head_cp.next.next`) and return the copy of a root of the original node._

---
- [x] Word Break (Medium)
> Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

e.g.
```
s = "applepenapple"
wordDict = ["apple","pen"]
# result: True - s can be segmented into "apple pen apple"
```

_DP top-down. State: `dp[s] = any([solve(s[i + 1:]) for i in range(len(s)) if s[:i + 1] in wordDictSet])`_

_DP bottom-up: `can_build[i]` denotes whether we can build a string `s[:i]`. We can build `s[:i]` if there exists some `j` between `0` and `i` for which `can_build[j] == True` and `s[j:i]` is in the set_

---
- [x] Linked List Cycle (Easy)
> Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

_Use Floyd's cycle detection algorithm_

---
- [x] LRU Cache (Medium)
> Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

_Use hash map with a doubly linked list. Note: create auxiliary `_add` and `_remove` methods for reassigning linked list pointers. Make sure to do the reassignment there only_

_Note: Python has an in-built `collections.OrderedDict` with methods: `move_to_end(key, last=True)` and `popitem(last=True)`._


---
- [x] Sort List (Medium)
> Given the `head` of a linked list, return the list after sorting it in ascending order.

_Use bottom-up merge sort for `O(1)` (see `SortList.py` for details)_

---
- [x] Max Points on a Line (Hard)
> Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

_For each pair of points compute a line `(slope, intersect)` and for each slope, keep a map `(slope, intersect) -> set(points on that line)`. Note that, since `float`s are not hashable by default, the key in the map is in the form `(slope_nominator, slope_denominator, intersect_nominator)` where fractions are in their simplest form. Use Euclid's `gcd` algorithm to determine those._

---
- [x] Evaluate Reverse Polish Notation (Medium)

> Evaluate the value of an arithmetic expression in Reverse Polish Notation.

_Use recrusive solution by parsing characters from the end one at a time. Note: In python `1 // -2 == -1` (not `0`). Use `int(a // b)` instead._

---
- [x] Maximum Product Subarray (Medium)

> Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

_`O(N)` scan, keeping two running values: `min_, max_` where `min_` and `max_` indicate the minimum and maximum product ending before the current number (not necessarily starting from the beginning of an array). When considering a given number, note its sign. If it's negative we can multiply it with  current `min_` to get the next `max_` (or multiply with current `max_` to get the next `max_` otherwise). We should **not** keep a cumulative product starting from the beginning of the array until current number, because this product might not be contiguous._

> e.g. `[2, 3, -1, 4]` - when considering `4` the maximum contiguous product would have been `6` but we cannot use `4` with `2, 3` to get a product of `24` because this would not be contiguous.

---
- [x] Min Stack (Easy)

> Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element `getMin` in constant time.

_When pushing an element, add to it an information about the current `min` in the stack (all elements below it)._

_Remark: See [here](https://cs.stackexchange.com/questions/6146/lower-bounds-queues-that-return-their-min-elements-in-o1-time) how to implement Queue with `O(1)` access to min element._

_Remark 2: Accessing `min` element and `pop`ing min element are different - the latter is not possible in `O(1)` - otherwise it'd allow you to sort in linear time_

---
- [x] Intersection of Two Linked Lists (Easy)

> Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`.

_Use `O(1)` memory by scanning the lists twice. First pass - calculate lengths of two lists. Second pass - Move the pointer on the longer lists by `diff` (where `diff` is a difference in lengths) and then move both pointers simultaneously until they meet._

---
- [x] Find Peak Element (Medium)

> A peak element is an element that is strictly greater than its neighbors.

Given an integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. Assume `nums[-1] = nums[n] = -inf`

_Solution in `O(logn)` with binary search. For a given `mid` element, search to it's left/right depending on which neighbour is greater. Neighbours cannot be the same height (as per constraint). If it was possible, linear search would not be possible (imagine an array `[1, 2, 1, 1, 1, 1, 1]` - for a mid element `1` the search procedure does not know which side (left/right) to search for a peak_
