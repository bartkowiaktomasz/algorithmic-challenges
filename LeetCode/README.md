# LeetCode - Top Interview Questions
Solutions to [**LeetCode - Top Interview Questions**](https://leetcode.com/problemset/top-interview-questions/)

- [x] Two Sum (Easy)
- [x] Add Two Numbers (Medium)
> You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 
0 itself.

> e.g. `l1 = 2 -> 4 -> 3`, `l2 = 5 -> 6 -> 4` gives `7 -> 0 -> 8`

_Iterate through both linked lists simultaneously while any of them is non-empty.
Add digits and carry a "carry" to the next operation in case of overflow_  

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
