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
  `n < e <= 0`


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
