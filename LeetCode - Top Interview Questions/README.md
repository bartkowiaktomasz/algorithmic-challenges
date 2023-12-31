# LeetCode - Top Interview Questions
Solutions to [**LeetCode - Top Interview Questions**](https://leetcode.com/problemset/top-interview-questions/)

- [x] 1. Two Sum (Easy)

---
- [x] 2. Add Two Numbers (Medium)
> You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 
0 itself.

> e.g.
```
l1 = 2 -> 4 -> 3
l2 = 5 -> 6 -> 4
gives 7 -> 0 -> 8
```

_Iterate through both linked lists simultaneously while any of them is non-empty.
Add digits and carry a "carry" to the next operation in case of overflow_

---
- [x] 3. Longest Substring Without Repeating Characters (Medium)
> Given a string `s`, find the length of the longest substring without repeating characters. Examples:
```
"abcabcbb" -> 3
"bbbbb" -> 1
"pwwkew" -> 3
"abba" -> 2
```

_Use sliding window approach with two moving pointers: `i, j`, `j > i`. Keep a set of `seen` letters. Expand `j` if `s[j] not in seen`. Once `s[j]` points to a letter thats `in seen`, shrink the window by incrementing `i` until `i` is to the right of the same letter that is currently being pointed to by `j`. In each round, keep track of the length of the largest substring window seen so far._

---
- [x] 4. Median of Two Sorted Arrays (Hard)
> Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, 
return the median of the two sorted arrays.

_This can be done in `O(min(logm, logn))`. Note that median is the number that cuts given list in half. First, you need to find a partition in a smaller list, where a partition is a cut that divides the list into two sublists. For a given partition we find a corresponding partition for the second list such that the number of elements in the left sublists `|LHS| == |RHS|` or `|LHS| == |RHS| + 1`. We know that the median is somewhere among the four boundary elements if a partition is a correct partition. The partition is correct iff max element of the LHS subarray (of one subarray) is smaller (or equal) to the min element of the RHS subarray (of the other list), e.g. the partitions below are correct because `5 < 6` and no element in the second list is smaller than `7`_
```
[1, 2, 5, | 7]
[| 6, 8
```
_NOTE: `|` indicates a partition. Finally, if the number of all elements is odd, return max element on the LHS (cause it's bigger), otherwise take an average of max LHS elem and min RHS elem._

---
- [x] 5. Longest Palindromic Substring (Medium)
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
- [x] 27. Remove element (Easy)

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
> Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).


_Note: Annoying edge cases like `input="++1"`_

---
- [x] Regular Expression Matching (Hard)

> Given an input string `s` and a pattern `p`, implement regular expression matching 
with support for `.` and `*` where: 

>`.` Matches any single character.

>`*` Matches zero or more of the preceding element.

> The matching should cover the entire input string (not partial).

_Use DP (bottom-up): Set up a boolean matrix of size `|S + 1| x |P + 1|` where `S` is the size of  a string and `P` is a size of a prefix. DP is useful because of the `*` (wildcard) case where we need to reuse previous (memoized matches), e.g._
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

_NOTE: DP State: `dp[i][j]`: `s[:i]` matches subpattern `p[:j]`_

---
- [x] Container With Most Water (Medium)
> Given `n` non-negative integers `a1, a2, ..., an`, where each represents a point at 
> coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of 
> the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the
> x-axis forms a container, such that the container contains the most water.

_O(n): (greedy) Use two pointers `i`, `j` that start at edges and get closer to each
other until they are equal. Increment `i` (or decrement `j`) whichever pointer points 
to the shorter line._

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
> Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

_Every approach needs to scan all characters in all strings so Best Conceivable Runtime (BCR) is `O(S)` where `S` is the sum of lengths of all strings_

---
- [x] 3Sum (Medium)
> Given an array nums of n integers, are there elements a, b, c in nums such that 
`a + b + c = 0`? Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

_Slow `O(n^2)`: Insert each `e`lement into a hash map and then check, for each pair of elements, if `-(a[i] + a[j])` is in the map_

_Optimised `O(n^2)`: Sort an array in `O(nlog)` (Note that you can solve 2Sum in `O(n)` so sorting is not needed there) and then, for each element `e` in the sorted array, keep two pointers `i`, `j` (`i` to the right of `e` and `j` at the end of the array) and increment/decrement the pointers depending on whether `sum > 0` or not._

_Optimisations:_
- #1: If `nums[i] == nums[i - 1]` then we're gonna find the same `l, r` and since we don't want to return duplicates, we can `continue`
- #2: If `e > 0` then the sum with `l` and `r` will be `> 0` (array is sorted) so we can `break`.

---
- [x] Letter Combinations of a Phone Number (Medium)
> Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order. A mapping of digit to letters (just like on the telephone buttons) is given below. Note that `1` does not map to any letters.

> e.g. `2 -> "abc", 3-> "def"` etc.

_Solve recursively by stripping `digits` (e.g. `234` -> `23` -> `2`) from the end  until one digit is left, then return a list of characters mapped to that digit. Merge this recursively with each letter corresponding to a current digit_  

---
- [x] Remove Nth Node From End of List (Medium)
> Given the head of a linked list, remove the nth node from the end of the list and return its head. Follow up: Could you do this in one pass?

_Scan the list with two pointers `i, j` with `j` being `n` nodes behind the `i`. In this way, when `i` hits the end, we know that the node at `j` needs to be removed_  

---
- [x] Valid Parentheses (Easy)
> Given a string s containing just the characters `'(', ')', '{', '}', '[', ']'`, determine if the input string is valid.

_Use stack to solve in `O(n)`. Optimisation: if input string has an odd length, return `False`_

---
- [x] Merge Two Sorted Lists (Easy)
> Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

---
- [x] Generate Parentheses (Medium)
> Given `n` pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

_Solve recursively. Start with empty string and, for each call, consider adding `(` or `)` at the end. Base cases should check if parentheses are valid, i.e. if, at any point, the number of `)` is `>` than the number of `(`. Keep track of the number of `(` and `)` used so far (e.g. `left`, `right`), once `left == right == n` we know it's a valid parentheses so we can append to the solution_

_Remark: The number of well-formed parentheses for `n` pairs of parentheses is `n`th Catalan Number so the solution scales with `O(4^n/n^(3/2))`_
  
---
- [x] Merge k Sorted Lists (Hard)
> You are given an array of `k` linked-lists lists, each linked-list is sorted in
ascending order. Merge all the linked-lists into one sorted linked-list and return it.

_Iterate each linked list simultaneously, adding new nodes to a priority queue. In each iteration, `heappop` smallest node from the heap, add it to the solution, access its `next` element and add that to the heap if it exists, otherwise add `inf`. `break` if the smallest element in the heap is `inf`._

---
- [x] Remove Duplicates from Sorted Array (Easy)
> Given a sorted array `nums`, remove the duplicates in-place such that each element 
appears only once and return the new length

_Use two pointers: slow runner `i` and fast runner `j`. Fast runner jumps over all duplicates until it hits a non-duplicate. Then we overwrite `nums[i + 1]` with `nums[j]` and increment both._ 

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
`divisor * 2^i` from `dividend` for each `i` we found in the inner loop until we get 
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

_First, find the index of the pivot and then decide, whether to do a binary search in the left or right sublist. Here pivot is defined as the first value of the  increasing subsequence which is smaller than the value on its left._

_Remark: `find_pivot` decides, in each step, whether to search the left or right part of the array based on whether `nums[mid] > nums[0]`_


---
- [x] Find First and Last Position of Element in Sorted Array (Medium)
> Given an array of integers nums sorted in ascending order, find the starting 
and ending position of a given target value.
> If target is not found in the array, return `[-1, -1]`.

_Implement two functions: `binary_search_leftmost` and `binary_search_rightmost` and then combine their outputs to give the starting and ending position of a target value_

_Remark: If numbers are `int`s it is sufficient to find an index of an input number `n` with `binary_search_leftmost` and then use `binary_search_leftmost` with `n + 1`._


---
- [x] Valid Sudoku (Medium)
> Determine if a 9 x 9 Sudoku board is valid. A valid sudoku does not have duplicate numbers in each row, each column and in each 3x3 subbox

_For each cell, check if any of the elements `(i, board[i][j]), (board[i][j], j), (i // 3, j // 3, board[i][j])` has been seen so far (if so - return `False`)._


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
  any positive number `> n` (e.g. `n + 1`) in the first pass, and ignore when doing next pass because we know that they won't be the answer (see p.1). After all, we ignore any element `e` such that `e > n or e <= 0`
- Return an index (+1) of the first non-negative number in the processed array which is `<= n`, e.g. for `[-1, -2, 4]` return  `3` (the input array was `[1, 2, 4]`).


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

_`O(N)` solution using stack. Stack keeps track of **indices** of bars. We will add a bar to the stack if it's smaller or equal to the top element on the stack - otherwise we pop bars until we encounter bigger (or equal) element and update the total area/volume for each popped bar. Note:_
- The reason for appending to stack bars smaller **or equal** is the fact that
once we encounter a bigger bar we will ignore the plateaus of bars with the same
heights and only add one big area at the end. E.g. say the heights are `[2, 1, 1, 1]` and we encounter `h = 4`. We will now start popping `1`s, adding the area of  `A = w * h = (current_idx - popped_idx - 1) * (min(1, 4) - 1) = 0` each time until we hit `2` where we add `A = w * h = (4 - 0 - 1) * (min(4, 2) - 1) = 3 * 1 = 3`.

- Note: For `O(n)` time and `O(1)` space use a two pointer approach - start with `left, right = 0, len(heights) - 1` and move them towards each other, updating trapped area. We can do it only if we move the pointer that points to a smaller bar (because we know that it is bounded from the other side by a higher bar)

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

Note: Solve by figuring out where an arbitrary point `(i, j)` will map after transformation. Assume `n, m` are height and width of the table and `i, j` are distance from the top and left edge of the table. After a 90 deg rotation, the point will map to `(j, m - i)`. Transposition: `(i, j) -> (j, i)` 

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

_Use [Kadane's Algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem) which runs in `O(n)`_

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
 keep track of one value *leftmost_good* which tracks the leftmost index 
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
> Given an `m x n` matrix. If an element is `0`, set its entire row and column to `0`. Do it in-place.

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

_Use three pointers: `left, mid, right = 0, 0, len(n) - 1` and swap elements while `mid <= right`. 
Swap according to the color encountered by `mid` - moving `0`s to the left by 
swapping with `left`, leaving `1`s in their place and moving `2`s to the 
right by swapping with `right`._ 

---
- [x] Minimum Window Substring (Hard)
> Given two strings `s` and `t`, return the minimum window in `s` which will 
contain all the characters in `t`. If there is no such window in `s` that covers 
all characters in `t`, return the empty string `""`. Note: `t` can contain
duplicates and the output window needs to contain all of them.

_Linear scan with two pointers: `i, j`. Use one loop: `j, char = enumerate(s, 1)` expanding `j` until all character have been seen. Maintain `need: Counter` (count of each letter that needs to be seen) and `count_needed: int` (how many unique letters need yet to be seen). When `count_needed == 0` start expanding `i` until `count_needed != 0`. Update `best_i, best_j` based on the size of the window `j - i`._

_Note: `enumerate(s, 1)` indexes `j` from 1 - this is to cover edge cases like `s = "a", t = "aa"`, where the answer `s[best_i:best_j + 1]` would return `a` instead of (correct) `""` (empty string)_

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

_Use stack of bar indices (heights can be looked up quickly given an index). The rep invariant in the stack is that, for a given bar, the bar to its left is necessarily smaller, so we only insert bars that are higher than the `top`. If we come across a bar that's smaller (or equal height) than `top` we pop the stack and calculate the area for each of the popped bars. The height of the area is the height of the popped bar. Insert dummy bar with `height = 0` at the end of the list to deal with an edge case._

---
- [x] 88. Merge Sorted Array (Easy)
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

_Iterative solution using `stack`. Keep track of `previous` node to compare it with `root` each time after retrieving it from the stack. If `previous.val >= root.val` at any time, the BST is invalid (Note the task imposes a constraint that BST keys (of children) must be strictly less or greater than the parent)._
 
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
- [x] 105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
> Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

_Note that: 1. First element of `preorder` is the `root`, 2. `inorder` array will look like `[..., root, ...]`. This means that for each element in `preorder` we can recursively build its left and right subtrees if we know the index of `root` element in the `inorder` array._

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

_Two scans: First, create a set of available numbers. In the second scan, for each number `n`, see how long consecutive sequence could be created starting at this number (a nested `while` loop). Trick: Do it only if `n - 1` is not in the available set. Say `nums = [1, 2, 3, 4]`. Thanks to this trick we'd only do a scan for `n = 1`. For `n = 2, 3, 4` the `while` loop wouldn't run_ 


---
- [x] Surrounded Regions (Medium)
> Given an `m x n` matrix board containing `'X'` and `'O'`, capture all regions surrounded by `'X'`. A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region. `'O'` is captured if it's not at the boundary or connected to the boundary by other `'O'`s

_BFS with `set` as a queue, searching from all `O`s at the borders of the `board`. Any `O` reachable from `O` at the border will not be captured - mark that cell with `K` (keep). After BFS, capture all `O` cells which haven't been changed to `K`._

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

_Use hash map with a doubly linked list (a.k.a. `LinkedHasMap`). Note: create auxiliary `_add` and `_remove` methods for reassigning linked list pointers. Make sure to do the reassignment there only_

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

_`O(N)` scan, keeping two running values: `min_, max_` where `min_` and `max_` indicate the minimum and maximum product ending before the current number (not necessarily starting from the beginning of an array). When considering a given number `num`, note its sign. If it's negative we can multiply it with  current `min_` to get the next `max_` (or multiply with current `max_` to get the next `max_` otherwise). When calculating `min/max` values for each `num` consider itself as well. Note: we should **not** keep a cumulative product starting from the beginning of the array until current number, because this product might not be contiguous._

> e.g. `[2, 3, -1, 4]` - when considering `4` the maximum contiguous product would have been `6` but we cannot use `4` with `2, 3` to get a product of `24` because this would not be contiguous.

---
- [x] Min Stack (Medium)

> Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element `getMin` in constant time.

_When pushing an element, wrap it into an object `StackElement` that also keeps track of the `min` in the stack (for all elements below it)._

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

_Solution in `O(logn)` with binary search. For a given `mid` element, search to it's left/right depending on which neighbour is greater. Neighbours cannot be the same height (as per constraint). If it was possible, binary search would not be possible (imagine an array `[1, 2, 1, 1, 1, 1, 1]` - for a mid element `1` the search procedure does not know which side (left/right) to search for a peak_

---
- [x] Fraction to Recurring Decimal (Medium)

> Given two integers representing the `numerator` and denom`inator of a fraction, return the fraction in string format.

```
numerator = 4, denominator = 333
# result: "0.(012)"
```

_Perform long division until we get a repeated `remainder` (store a map from remainders to their position in a hash map)._

---
- [x] Majority Element (Easy)
> Given an array `nums` of size `n`, return the majority element (elemen appearing more than `n // 2` number of times)

_Use **Boyer-Moore Voting Algorithm** to solve in `O(n)` time and `O(1)` space (see code for explanation)_

---
- [x] Excel Sheet Column Number (Easy)

> Given a string `columnTitle` that represents the column title as appear in an Excel sheet, return its corresponding column number.

```
e.g. columnTitle = "AB"
# result: 28
```

---
- [x] Factorial Trailing Zeros (Easy)
> Given an integer `n`, return the number of trailing zeroes in `n!`.

_Solution in `O(logn)`: Use the fact that:_
```
n! = 1 * 2 * ... * 5 * ... * 10 * ... 15 * ... * 25 * ... * n
```
_The number of trailing 0s will come from the number of `10`s, i.e. the `min` number of `2`s and `5`s if we factorize `n` to primes. e.g. `k = 2 * 2 * 2 * 5 * 5` has `min(2, 3) = 2` number of trailing zeros._

_Remark: In the factorial, there will always be more (or equal) `2`s than `5`s in the factorization so we only need to find the number of `5`s in the factorized form._

---
- [x] Largest Number (Medium)

> Given a list of non-negative integers nums, arrange them such that they form the largest number.

```
Input: nums = [10,2]
Output: "210"

Input: nums = [3,30,34,5,9]
Output: "9534330"
```

_Sort using custom comparator (`key`) and concatenate all numbers. The `key` should sort based on the value of concatenated two numbers that are being compared. e.g. `3 > 30` because `330 > 303` (we concatenate `3` and `30`)._

---
- [x] Rotate Array (Medium)
> Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

_Use cyclic replacements - start from an element, put it in it's destination position and then do the same for the replaced element. Note that this might need to be performed multiple times (each time starting with a different element) in case of cycles. It's sufficient to do replacements for elements starting at `idx = [0, 1, ..., k]`_

_Remark: We can also solve the problem by reversing an array: `reverse(nums) -> reverse(nums[:k]), reverse(nums[k:])`_

```
Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
```

---
- [x] Number of 1 Bits (Easy)

> Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

---
- [x] House Robber (Medium)

> Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

_Use DP with state: `dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])`_


---
- [x] Number of Islands (Medium)
> Given an `m x n` 2D binary grid grid which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

_Use BFS. Optimisation: Instead of using `set` for marking `visited`, mark them directly in the input grid_

---
- [x] Happy Number (Easy)
> Write an algorithm to determine if a number `n` is happy. A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

_Solution with `O(1)` memory uses Floyd's cycle detection (we don't need to store numbers that we've seen already to be able to detect a cycle). Whenever fast pointer hits `0` the number is guaranteed to be happy._

---
- [x] Count Primes (Easy)
> Count the number of prime numbers less than a non-negative number, `n`.

_Use the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)_

---
- [x] Reverse Linked List (Easy)
> Given the `head` of a singly linked list, reverse the list, and return the reversed list.


---
- [x] Course Schedule (Medium)
> There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where p`rerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses. Otherwise, return `false`.

_Build a graph and use DFS to find if it has cycles. If so - return `False`. A directed graph has a cycle if there exists a backward edge in a graph. Keep a track of a state list `visited` with 3 states: `-1` if a node is being visited in a current DFS run, `0` if it has not been visited and `1` if it has been visited._

---
- [x] Implement Trie (Medium)
> Implement Trie data structure

---
- [x] Course Schedule II (Medium)
> There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where p`rerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses. Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

_Return a toposort of the courses. Here, use [Kahn's algorithm](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm) to do a BFS-based toposort (no recursion as in DFS)_

---
- [x] Word Search II (Hard)
> Given an `m x n` board of characters and a list of strings `words`, return all `words` on the board. Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

_Build a trie from `words` and then perform DFS of the `board`_

_Optimisation: Mark nodes that are currently being visited in DFS run as `#` in-place to save space_

_Optimisation 2: When doing DFS we simultaneously walk down the Trie. We can use `node.end` to look-up whether we've just discovered a word defined in `words`_

---
- [x] Kth Largest Element in an Array (Medium)
> Given an integer array `nums` and an integer `k`, return the kth largest element in the array. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

_Use QuickSelect for average `O(N)` performance. In the partitioning procedure make sure that, after partitioning, every element at idx `i < pivot_idx` is smaller than `pivot` and anything `j > pivot_idx` is greater or equal than `pivot`._

_Remark: Try partitioning the array `nums` based on boundaries `low, high` and not by slicing the array at each iteration_

---
- [x] Contains Duplicate (Easy)
> Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

_[Element distinctness problem](https://en.wikipedia.org/wiki/Element_distinctness_problem) states that, for arbitrary `nums` and without extra space, best runtime is `O(NlogN)`_

---
- [x] Skyline Problem (Hard)
> A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively. Question: https://leetcode.com/problems/the-skyline-problem/

_1. Split buildings into single points `(x, h, type)` and mark each point whether it is a left (`-1`) or a right (`1`) point of a given building._

_2. Update the result if the max height **of the priority queue changes:** skyline is formed by changing max heights_

_3. Sort points based on three conditions: (X position, type, height)(in this order). Left needs to be before Right (imagine what happens if there are two buildings same height, right side of first one overlaps  with the left side of the next one). Height-wise, if we have two left points  (same x), higher needs to be considered first. If two right points, consider the lower one first._

---
- [x] Basic Calculator II (Medium)
> Given a string `s` which represents an expression, evaluate this expression and return its value. Example: `s = "3+2*2"` return `7`.

_Use Stack. First, preprocess the string to build a stack with numbers and operations. Then parse elements in the stack left to right (i.e. from the bottom, like a queue). Each time pop three elements (left operand, operation, right operand) and if it's addition/subtraction, update the result. Otherwise evaluate the operation and put it back on the stack. If there is one (last) element in the stack, add it to the result and return._

---
- [x] Kth Smallest Element in a BST (Medium)
> Given the root of a binary search tree, and an integer `k`, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

_Do an in-order traversal (it sorts a BST). Keep a global count of unique elements seen so far and return immediately when seeing `k`th unique element._

---
- [x] Palindrome Linked List (Easy)
> Given the `head` of a singly linked list, return true if it is a palindrome.

Idea: Revert the first half of the list and then iterate
simultaneously with two pointers: one traverses from mid to start
and the other one traverses from mid to end.
```
    e.g. 1 -> 2 -> 3 -> 2 -> 1 change to: 1 <- 2 <- 3 -> 2 -> 1
    e.g. 1 -> 2 -> 2 -> 1 change to: 1 <- 2  2 -> 1
```
1. Use two pointers: slow, fast to find the mid of the list
2. Iterate from the list start reversing its direction until we hit list's mid
3. Iterate two pointers from mid, one towards the start, one towards the end
to decide if palindrome

---
- [x] Product of Array Except Self (Medium)
> Given an integer array `nums`, return an array answer such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Build two arrays: `prefix_product` and `suffix_product` such that `prefix_product[i]` contains the product of all elements before `i` (excluding `i`). Likewise,
`suffix_product[i]` contains the product of all ements after `[i`] (excluding `i`). The result is `prefix_product[i] * suffix_product[i]` for all `i`. Note: one can store `prefix_product` directly in the result and then iterate backwards with a single `suffix_running_product` variable, updating the `result`.

---
- [x] Sliding Window Maximum (Hard)
> You are given an array of integers nums, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Use monotonic (non-increasing) queue (`deque_`). When we iterate through input, `deque_[0]` will contain the index of the largest element in the current window. If this index is outside the current window, we'll pop it. 

---
- [x] Search a 2D Matrix II (Medium)
> Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
> - Integers in each row are sorted in ascending from left to right.
> - Integers in each column are sorted in ascending from top to bottom.

There is no simple logarithmic solution. $O(m + n)$ starts in the top-right corner and eliminates one row or column at a time (depending whether $m[i][j]$ is greater than or smaller than the target).

---
- [x] Valid Anagram (Easy)
> Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and false otherwise.

Compare counts of characters in both strings

---
- [x] Missing Number (Easy)

> Given an array nums containing n distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

Return a XOR of `x1` and `x2`, where `x1` is a XOR of all elements `0,...,n` and `x2` is a XOR of all elements in the input `nums`. The XOR of `x1, x2` will eliminate (set to zero) every `1` bit that was present in both. What's left is an element that is in one but not the other array.

Alternatively, use the fact that the sum of all elements `1,...,n` is `n/2*(1+n)`

---
- [x] Perfect Squares (Medium)
> Given an integer `n`, return the least number of perfect square numbers that sum to `n`.

Use Dynamic Programming

---
- [x] Move Zeroes (Easy)
> Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.

Use two pointers (`slow` and `fast`). `slow` points to a zero element. Iterate `fast` until it points to a non-zero element. Swap.

---
- [x] Find the Duplicate Number (Medium)
> Given an array of integers nums containing n + 1 integers where each integer is in the range `[1, n]` inclusive. There is only one repeated number in nums, return this repeated number.

- (Optimal) `O(N)` time and `O(1)` space: Travel around the input list like through a linked list (current number indicates the next index to go to). Duplicate number will cause a loop in the list. Use Floyd's cycle detection algorithm to determine the duplicate. Note: The first number/node in the loop is not the duplicate, it's the node before!
- `O(NlogN)` time - Binary search over the answer - count the number of elements smaller/bigger than `x` and search over `x` (initialise `x = n // 2`).

---
- [x] Game of Life (Medium)
> Given the current state of the `m x n` grid `board`, return the next state (as per the Game of Life rules)

- For each cell, find its next state and save it in `board[i][j]` itself. As a memory optimisation we can (in each cell) store 2 bits, where the first (leftmost) bit represents current cell state and the second bit represents the next state. In the second pass, we shift the 2bit number to the right, only leaving the next state.


---
- [x] Find Median from Data Stream (Hard)
> Given a datastream, implement `addNum` and `findMedian`

- Use two heaps: `smaller` (max heap) and `larger` (min heap) to keep smaller half and larger half of numbers (respectively). Note: the `addNum` should first `heappush` onto one heap, then `heappop` from it and `heappush` that element onto the other heap. Optimisation: Use `heapq.heappushpop`.

---
- [x] Serialize and Deserialize Binary Tree (Hard)
> Design an algorithm to serialize and deserialize a binary tree

- Use pre-order or level-order tree traversal

---
- [x] Longest Increasing Subsequence (Medium)
> Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

- Use [Patience sorting](https://en.wikipedia.org/wiki/Patience_sorting) ([Princeton notes](https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf)) for `O(nlogn)`. Alternatively, use DP where `dp[i]` is the minumum (ending) value which is the end of increasing sequence of length `i + 1`. So e.g. with `[1, 2, 4, 3]` we will iterate through all the numbers and update the `dp` to be `[1] -> [1, 2] -> [1, 2, 4] -> [1, 2, 3]`. Return the length of the list. Use `bisect.bisect_left` to find an appropriate index where to insert a number.

---
- [x] Count of Smaller Numbers After Self (Hard)
> You are given an integer array `nums` and you have to return a new `counts` array. The `counts` array has the property where `counts[i]` is the number of smaller elements to the right of `nums[i]`.

- Use (a modified) merge sort to count the number of inversions for each number. An inversion, for a given number `x` is when there is some other number `y` smaller than x that gets put to the left of `x` when doing the merge sort.  Note: When we have, in the "combine" step of the merge sort, e.g. `left=[2, 3, 5, 6], right=[1]`, do not increment the counter for `2, 3, ..., 6` before appending `1` to the combined list. This will result in `O(n^2)` worst case time in the combine step.

---
- [x] Coin Change (Medium)
> You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount.

- Use DP

---
- [x] Wiggle Sort II (Medium)
> Given an integer array nums, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]` ...

- Sort `nums` and split into `smaller, bigger` halves. Overwrite `nums` by injecting numbers from `smaller/bigger`, alternating between them. Note: Need to iterate through `smaller/bigger` backwards - consider the input `[4, 5, 5, 6]`.

---
- [x] Power of Three (Easy)
> Given an integer `n`, return `true` if it is a power of three. Otherwise, return `false`. Follow up: Could you solve it without loops/recursion?

- Use `math.log(n, 3) % 1` and then compare against `0` or `1` using `math.isclose`. Alternative solution: `x = 3 ** 19` is the highest power of 3 that fits in 32-bit int. 3 is prime so only the powers of 3 will divide `x`.

---
- [x] Odd Even Linked List (Medium)
> Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

- Reorder by performing a single scan with two pointers

---
- [x] Longest Increasing Path in a Matrix (Hard)
> Given an `m x n` integers `matrix`, return the length of the longest increasing path in `matrix`.

- Use DP

---
- [x] Increasing Triplet Subsequence (Medium)
> Given an integer array `nums`, return true if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exists, return false.

- Use [Patience sorting](https://en.wikipedia.org/wiki/Patience_sorting) ([Princeton notes](https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf)) for `O(nlogn)` or DP with binary search as in the _Longest Increasing Subsequence_ problem.

---
- [x] Flatten Nested List Iterator (Medium)
> You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it. e.g. `[[1,1],2,[1,1]] -> [1,1,2,1,1]`

- Use a `deque` - keep unpacking the first element, appending all its elements back to the `deque` until the first element is an integer.

---
- [x] Reverse String (Easy)
> Write a function that reverses a string. The input string is given as an array of characters `s`.

---
- [x] Top K Frequent Elements (Medium)
> Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

> Count the occurences of all elements and then add them to heap of (a fixed) size `k`

---
- [x] Intersection of Two Arrays II (Easy)
> Given two integer arrays `nums1` and `nums2`, return an array of their intersection.

> Use `Counter(nums1) & Counter(nums2)`

---
- [x] Sum Of Two Integers (Medium)
> Given two integers `a` and `b`, return the sum of the two integers without using the operators + and -.

> Perform `XOR` while `carry` is non zero

---
- [x] Kth Smallest Element in a Sorted Matrix (Medium)
> Given an `n x n` matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

- The answer is the smallest number `x` (found via binary search in the range `min(matrix), max(matrix)`*) out of all elements that have the property that _"the number of elements in the matrix which are less-or-euqal-to that element is `>= k`"_. Note: during the binary search, the `mid` element doesn't necessarily need to be in the matrix.

- The efficient way to find, for a given element, the number of elements in the matrix which are less-or-euqal-to that element is, roughly, to count the elements by starting in the top-right corner of the matrix and moving down-left (whichever makes sense based on the current number)

---
- [x] Insert Delete GetRandom O(1) (Medium)
> Implement the `RandomizedSet` class with `O(1) insert, remove, getRandom` (average).

- Keep an array with elements `self.nums` and a dictionary with their positions in the array `self.idxs = {num: arr_idx}`. When removing, replace removed element with the last element from the array (and update the dictionary accordingly).

---
- [x] Shuffle an Array (Medium)

> Given an integer array `nums`, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

- Iterate through an entire array - each time swapping current element at index `i` with a random element at position  `[i, len(n) - 1]`

---
- [x] First Unique Character in a String (Easy)

> Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

- One-pass solution using Doubly Linked list and a `map: char -> node`. The doubly linked list contains elements seen only once (so that the last element of the list is the answer).

---
- [x] Longest Substring with At Least K Repeating Characters (Medium)

> Given a string `s` and an integer `k`, return the length of the longest substring of `s` such that the frequency of each character in this substring is greater than or equal to `k`.

Recursive solution by splitting the original string into substrings using least frequent character (assuming its frequency is ` <k`). If, given a substring `sub`, the east frequent character has the frequency `>= k`, return `len(subs)`.

---
- [x] Fizz Buzz (Easy)

---
- [x] 4Sum II (Medium)

> Given four integer arrays `nums1`, `nums2`, `nums3`, and `nums4` all of length `n`, return the number of tuples `(i, j, k, l)` such that `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`. 

- `O(n^2)`: Count sums of all pairs of numbers of `nums1, nums2` (1) and repeat for `nums3, nums4` (2). Then, for each sum in (1) check if `-sum` is in (2).

