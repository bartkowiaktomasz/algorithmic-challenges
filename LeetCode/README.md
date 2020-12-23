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
- [x] Regular Expression Matching

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
- [x] Container With Most Water
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
