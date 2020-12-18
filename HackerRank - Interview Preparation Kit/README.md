
# HackeRank - Interview Preparation Kit
Solutions to [**HackerRank Interview Preparation Kit**](https://www.hackerrank.com/interview/interview-preparation-kit)

## Warm-up Challenges
- [x] Sales by Match (Easy)
- [x] Counting Valleys (Easy)
- [x] Jumping on the Clouds (Easy)
- [x] Repeated String (Easy)

## Arrays  
 - [x] 2D Array - DS (Easy)
 - [x] Arrays: Left rotation (Easy)  
 > A _left rotation_ operation on an array shifts each of the array's elements unit to the left.
 - [x] New Year Chaos (Medium)
 > Find the minimum number of bribes (swaps) that took place to get the queue into its 
   current state. One person can bribe at most two others.
 > e.g. `[1, 2, 3, 5, 4]` means one bribe (Person 5 swapped a position with Person 4)

   Start from the left (top). For each person in the queue count the number of times
   given person was bribed. Also, since we can only do two bribes, any person that bribed 
   person `P` cannot get further top than one position in front of `P`s *original* position 
   and further back than `P`s current position
 - [x] Minimum Swaps 2 (Medium)
 > You need to find the minimum number of swaps required to sort the array in ascending order.

1. Sort an array `arr` to get `arrSorted`
2. Create a hashmap `d` of each element in the sorted array to its position (index) in that array
3. Identify all cycles in the original array (e.g. for `[1, 3, 4, 2]` there is one cycle
    `3 -> 4 -> 2 (-> 3)`) using `d` and `arrSorted` (we know that e.g. `3` needs to go
    to index/position `2`)
4. Each cycle with size `n` can be ordered with `n - 1` swaps because each swap places
one element in the correct position (last swap will place two elements in their positions)
 - [x] Array Manipulation (Hard)
> Starting with a 1-indexed array of zeros and a list of operations, for each operation
  add a value to each of the array element between two given indices, inclusive.
  Once all operations have been performed, return the maximum value in the array.
> e.g. operation `o = [a, b, k]` means indices `a, b` and the value of `k`, 
> e.g. for `n=5` and query/operation `[1 2 3]` we do:
```
[0, 0, 0, 0, 0] -> [3, 3, 0, 0, 0]
```

Given `l` to be our initial list of `0`s:
1. For each query `[a, b, k]` add the value of `k` to `l[a-1]` and `-k` to `l[b]` such
that we only alter two cells - the first changed cell and the first unchanged cell.
2. After making all queries, the cumulative sum for each cell will represent its value.
In the example above (`[1 2 3]`) we do:
```
[0, 0, 0, 0, 0] -> [3, 0, -3, 0, 0]
```
Then we know that the running cumulative sum is `[3, 3, 0, 0, 0]`. This improves the
running time cause we only overwrite two cells for each query. 

## Dictionaries and Hashmaps  
- [x] Hash Tables: Ransom Note (Easy)
> Given the words in the magazine and the words in the ransom note, print `Yes` if he can replicate his ransom note _exactly_ using whole words from the magazine; otherwise, print `No`.

 _Insert each word from `magazine` to a dict (char as a `key` and counter as a `value`) and then, for each word in `ransom note` check if the word is available._   

- [x] Two Strings (Easy)
> Given two strings, determine if they share a common substring. A substring may be as small as one character.
 
 _It is enough to check if strings share at least one common letter._

 - [x] Sherlock and Anagrams (Medium)
 > Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
 Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
 
 _For each substring, sort its letters it and store the counter for each sorted substring in a hash map. Then for each element in the hash map
 calculate the number of anagrams, which can be interpreted as a number of connections with other identical sorted substrings 
 (number of connections between the vertices of the polygon, i.e. `n(n-1)/2)`._
 
 _Optimisation: Use rolling hash (e.g. Rabin-Karp) and use a hashing function that
 gives the same hash to anagrams (this eliminates the sorting step)._
 
 - [x] Count Triplets (Medium)
 > You are given an array and you need to find number of tripets of indices
`(i, j, k)` such that the elements at those indices are in geometric progression
for a given common ratio `r` and `i < j < k`

> e.g. for `arr = [1, 4, 16, 64]` if `r = 4` we have `[1, 4, 16]` and `[4, 16, 64]` at 
indices `(0, 1, 2)` and `(1, 2, 3)` so the count is `2`.

_This algorithm can be solved in linear time with one pass: 
Run a single pass through the array and for each element `elem` keep track how many
previous elements can form a tuple `(i, j)` and triple `(i, j, k)` with `elem`.
Keep two counters for that purpose, e.g. `t2`, `t3`. For example, if for one of
the elements no other elements are yet to form a tuple or triple, this element
is the one that is "waiting" to form a tuple and then a triple. For this purpose
increment the counter (`t2`) for the value `elem*r`. Next time, if element `elem*r`
arrives, it will check how many elements are waiting for it and will increment
the value of `t3` accordingly._

- [x] Frequency Queries (Medium)
> You are given `q` queries. Each query is of the form two integers described below:
 1 Insert, 2 Delete, 3 Check. Process the those queries and report if any integer
 is there with a particular frequency.

_Keep a mapping from the integer to its count and a mapping from a count to the
set of integers. Increment/decrement counters when needed and return true if,
when queried, the size of the set of integers with given count is greater than 
zero_

- [x] Fraudulent Activity Notifications (Medium)
> HackerLand National Bank has a simple policy for warning clients about possible 
fraudulent account activity. If the amount spent by a client on a particular day is
greater than or equal to  the client's median spending for a trailing number of days,
they send the client a notification about potential fraud. The bank doesn't send the
client any notifications until they have at least that trailing number of prior days' 
transaction data.

> Given the number of trailing days `d` and a client's total daily expenditures
for a period of `n` days, find and print the number of times the client will
receive a notification over all `n` days.

_Note that the range of expenses is very small (0-200), which allows it to be
sorted using count sort, which is linear time. Create a cumulative
sum array (count sort array) to keep all the expenses that need to be used to
compute the median. Each time add remove the last expense and add a newest one 
and propagate the change throughout the array. The median can be efficiently
found using `bisect` (binary search) from the cumulative count array._
 
 ## Dynamic Programming
- [x] Max Array Sum (Medium)
> Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
Calculate the sum of that subset.

_Bottom up solution: Build an array (dynamically) that, at each position, holds a maximum 
sum of the original array up to that position. For each next element (at position `i`)
the maximum sum will either be a) the element itself, b) previous max sum 
(at position `i-1`), or c) sum of that element and the maximum sum at position `i-2`._

- [x] Candies (Medium)
> Alice is a kindergarten teacher. She wants to give some candies to the children in her class. 
All the children sit in a line and each of them has a rating score according to his or her performance
in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each
other, then the one with the higher rating must get more candies. Alice wants to minimize the total 
number of candies she must buy.

_Create two arrays: `left_to_right` and `right_to_left`. The first array will keep the 
amount of candies such that each child with higher score than its left neighbour will 
have more candies. The other array ensures the reverse. The return value will be the
max of the two at each position. Note that this solution is `O(N)` in both time and 
space and there exists a solution that is `O(1)` in space:
[Solution on LeetCode](https://leetcode.com/problems/candy/solution/)_

- [x] Abbreviation (Medium)
> You can perform the following operations on the string, `a`:
> 1. Capitalize zero or more of `a`'s lowercase letters.
> 2. Delete all of the remaining lowercase letters in a.

> Given two strings, a and b, determine if it's possible to make `a` equal to `b` as 
> described. If so, print YES on a new line. Otherwise, print NO.

_Use `dict` for memoization. Set `sys.setrecursionlimit(2000)` to allow for 
 bigger stack. Do not memoize tuples of strings but tuples of indices instead. 
 Remember, in `if` statements, to put statements that are easier to evaluate
 on the left hand side so that, if the result is `False`, short-circuting
 prevents from evaluating expensive expression (e.g. `string.lower()`)._


 
 ## Graphs
 - [x] Find Nearest Clone (Medium)
 > In this challenge, there is a connected undirected graph where each of the
nodes is a color. Given a color, find the shortest path connecting any two
nodes of that color. Each edge has a weight of 1. If there is not a pair or if
the color is not found, print -1.

_Use BFS to find the shortest path which gives `O(|V| + |E|)`_

 - [x] Roads and Libraries (Medium)
> HackerLand has `n` cities numbered from `1` to `n`. The cities are connected by `m`
bidirectional roads. A citizen has access to a library if: 1) Their city contains a
library and 2) They can travel by road from their city to a city containing a library.

 > You are given ``n`` queries, where each query consists of a map of HackerLand
and value of ``cost_library`` and ``cost_road``. For each query, find the minimum
cost of making libraries accessible to all the citizens and print it on a
new line.

_This is a graph question. First, compute the number of components in the graph
(and how many vertices there are in each component) - this can be done using 
`DFS` or `BFS` (here `DFS` is used). If the library is cheaper than the road, 
build a library in each city. Else build one library per component. The number
of roads in the component is the number of vertices (cities) minus one. Sum
the costs for all of the components._

 - [x] BFS: Shortest Reach in a Graph (Hard)

_Use BFS_
 - [x] DFS: Connected Cell in a Grid (Hard)
 > Find the biggest region in a binary matrix. Region is a set of matrix cells that
have the value of `1` and are adjacent to each other (vertically, horizontally or 
diagonally)

_Use DFS to traverse the regions. Keep track of visited cells (e.g. in another matrix)_
 - [x] Matrix (Hard)
 > The kingdom of Zion has cities connected by bidirectional roads. There is a
   unique path between any pair of cities. Morpheus has found out that the machines
   are planning to destroy the whole kingdom. If two machines can join forces,
   they will attack. Neo has to destroy roads connecting cities with machines in
   order to stop them from joining forces. There must not be any path connecting
   two machines.

 > Each of the roads takes an amount of time to destroy, and only one can be
   worked on at a time. Given a list of edges and times, determine the minimum
   time to stop the attack.
   
 > TLDR: Given a graph with green and red nodes and weighted edges, define
   the edges with the least cost that, when removed, result in disjoint graphs
   that have at max one red node.

_Sort the edges by decreasing weight. Then, for each edge, build graph
Components (biggest weights are used to build the components, which means
we will remove the lightest edges). Use given edge to connect the nodes iff
the components they belong to do not make a graph with two red nodes (machines). 
This can be tracked by using Union-Find (DisjointSet) structure, where the parent
holds information about whether there is already a red node (machine) in the 
component. If both components have a red node inside them this means that given
edge needs to be removed (increase the time counter). Use `path compression` to
speedup union/find operations._

_NOTE: This is a modification of a Kruskal's algorithm (we're trying to find a Minimum
Spanning Tree (MST) using Union-Find (Disjoint-Set)) which builds an MST by sorting
existing edges in order._

 
## Greedy Algorithms 
- [x] Minimum Absolute Difference in an Array (Easy)
> Given an array of integers, find and print the minimum absolute difference between 
any two elements in the array.

_Sort and compute running diff => O(nlogn). You can theoretically do O(dn) where `d` is
the minimum absolute difference by adding all elements to a set and for each element
checking_

- [x] Luck Balance

- [x] Greedy Florist
> Minimize the amount of money it costs for a group of friends to 
buy all 'n' flowers

_Sort an array and then, until all flowers are bought, add (for
each friend) the most expensive ones to the sum (the amount of additional money we
need to pay later is linear in `c[i]` so we want to buy the most expensive flowers first,
at the lower multiple). Also we need to keep track of the `round number` (in each turn
the cost of flowers increases)._

- [x] Max Min
> You must create an array of length `k` from elements of `arr` such that its
unfairness is minimized (unfairness is a diff between the max and the min elements).

_Sort an array and find a sliding window of size ``k`` for which the
difference between the biggest and the smallest element is the smallest._

- [x] Reverse Shuffle Merge
> Given a string S such that `s = merge(reverse(A), shuffle(A))` for some string
> `A`, find the lexicographically smallest `A`.
> "shuffle" is any permutation of the string
> "merge(a, b)" is an interspersing of "a" and "b" that maintains the order
  of the characters

_First of all, note that in the input string `S` every character of `A` is 
duplicated. Also, if we `reverse(S)` and iterate it, we will get a `A` as a
subsequence. So, while iterating `reverse(S)` we must select some characters
and reject others to build `A`. The key is that sometimes we need to backtrack when coming
across some reasonably "small" character. For this purpose it is useful to
use an `answer` array as a stack, and each time we find a "good" character,
we can pop as many characters from the `answer` stack as necessary (assuming some
conditions are met). We also need to build `freq` tables for keeping track of 1) 
count of each character that we still need to use (we know all the characters of `A`
upfront) and 2) count of chars that are yet to be seen in the string while iterating.
Whenever we get a char that is smaller (i.e. better) than the one on top of the stack, 
we can start popping the elements all the way down the stack if and only if they
are bigger than our current `char` and if we are yet to see sufficient number
of those characters in future._

## Linked Lists  
- [x] Linked Lists: Detect a cycle      
> Given a linked list detect if it contains a cycle.

 _Use Floyd's cycle detection algorithm - create two pointers, one (slow) jumping from list to the next node, the second one (quick) jumping to every 2nd node. If they eventually meet, there is a loop._    

- [x] Inserting a Node Into a Sorted Doubly Linked List  
> Given a reference to the head of a doubly-linked list and an integer, `data`, create a new DoublyLinkedListNode object  
having data value `data` and insert it into a sorted linked list while maintaining the sort.

- [x] Reverse a doubly linked list   
> You’re given the pointer to the head node of a doubly linked list. Reverse the order of the nodes in the list.

- [x] Insert a node at a specific position in a linked list
- [x] Find Merge Point of Two Lists

## Miscellaneous  
 - [x] Bit Manipulation: Lonely Integer
 - [x] Time Complexity: Primality
 - [x] Flipping Bits
 > You will be given a list of 32 bit unsigned integers.
 Flip all the bits and print the result as an unsigned integer.

_`XOR`ing with `one` will flip the beats of any binary number._

 - [x] Maximum XOR
 > You are given an array `arr` of `n` elements. A list of integers, `queries` is
   given as an input, find the maximum values of `queries[j] xor arr[i]` for all `i`.

_First, build a binary trie out of all `arr` numbers. Then, for each element of 
`queries`, convert the element to bits and traverse the trie to find the 
maximum `xor` value. The trick is, when traversing, go to the opposite bit than
the current bit (because in order for `xor` to be `1` the args must be opposite)
if it's possible, otherwise go to the same direction (the resulting `xor` bit
will be zero in such case). For each of the bits, append them to the list and, at the
leaf node, convert the list to string and return it as a `max` value for given
`query`._

- [x] Friend Circle Queries
> You will be given q queries. After each query, you need to report the size of
the largest friend circle (the largest group of friends) formed after
considering that query.

_Use `Union-Find` (or `Disjoint-Set`) data structure, which has a linear time
or almost constant amortized time for `union` and `find`, when both path
compression and union by rank/size are applied._ 

## Recursion and Backtracking
- [x] Recursion: Fibonacci Numbers
> Implement Fibonacci sequence recursively.
- [x] Recursion: Davids' Staircase
> Complete the  _stepPerms_  function in the editor below. It should recursively calculate and return the integer number of ways Davis can climb the staircase, modulo 10000000007.
- [x] Crossword Puzzle
> Fill in the crossword of size 10x10 with given list of words.

_Build a pool (stack/set) with all positions to which words are to be inserted. 
For each position try inserting words recursively. `Revert` function (cleaning wrong 
entries) is called twice: first time when insertion was successful (proper
word length) but recursive `solve` returned `False`, and the second time
when no words fit given position (the current position itself should be put 
back to the pool)._

- [x] Recursive Digit Sum
> Calculate a `super digit` of given number recursively until one digit is 
left, e.g `sd(533) = sd(5+3+3) = sd(12) = sd(1+2) = sd(3) = 3`


## Search  
- [x] Hash Tables: Ice cream parlor      
> Given list of integers, find two of them that sum to n.  
  
_Iterate through the list once and add each value to the dict if it does not already contain an element that, when added, gives a sum of n._   

- [x] Swap Nodes   
> Build a Binary Tree and swap children of nodes at particular depths.
After each round of swapping, traverse the tree in-order and print the values of nodes.

_Build a tree using queue, for each pair of children to be inserted, pop a parent from the queue
and add children to it._

- [x] Pairs
> You will be given an array of integers and a target value.
Determine the number of pairs of array elements that have a
difference equal to a target value.

_Use `hashmap` to store each element of the array. Then in the second pass
check `hashmap` for the existence of `elem+k` and `elem-k`. Return `num_pairs/2` 
because each existing pair has been counted twice._

- [x] Triple Sum
> Sum of special triplets having elements from 3 different arrays.

_First sort the arrays and remove the duplicates. Then iterate through the
arrays in parallel, counting for each element `elem` of array `b` the number of
elements in `a` and `c` that is less or equal to `elem`. The number of possible
triplets for each `elem` is the product of the counts_.

- [x] Minimum Time Required
> You are planning production for an order. You have a number of machines that
each have a fixed number of days to produce an item. Given that all the
machines operate simultaneously, determine the minimum number of days to
produce the required order.

_First sort the machines. Then we need to find a minimum find of days that give
particular `goal` (and one day less must give a value less than a `goal`). 
This is a binary search question where days are the arrays we operate in. 
The bounds for days are `1` and `10^18` since in the worst case there is only
one machine that needs `10^9` days to produce an item and we need `10^9` items.
Recursion might be too deep so we need to use two moving bounds to iteratively 
keep track where we are. Util function `num_items` will, given a number of days,
output a number of items that the `machines` can produce._

- [x] Maximum Subarray Sum
> Find a maximum subarray sum of given array such that the `sum(subarr) mod m` is the
biggest. 

NOTE that a subarray is contiguous and a subsequence is not. In the algorithm
it is useful to build a prefix sum table such that `prefix[n] = (a[0] + ... a[n]) mod m`.
Then it is important to note that the highest modulo for each `prefix[i]` will
be for some `prefix[j]` such that `(prefix[i] - prefix[j]) % M` is the biggest. 
For this reason `prefix[j]` must be bigger by `prefix[i]` but ideally only bigger by `+1`,
because then the modulo will be `M-1`. So we need, for each `prefix[i]`, to be
able to find `prefix[j]` which is bigger but as close as possible to `prefix[i]` 
as possible. We cannot first build the `prefix` table and then sort it because
we lose track of indexes and we can only subtract `prefix[i]` from `prefix[j]` if 
`i > j` (they need to be contiguous). So we need to dynamically create a prefix
table and keep it sorted. In order to get an index of the element which is closest
to our current new prefix table element, we can use `bisect.bisect_right`.
 
- [x] Making Candies
> Karl loves playing games on social networking sites. His current favorite is
  CandyMaker, where the goal is to make candies.
  Karl just started a level in which he must accumulate `n` candies starting with
  `m` machines and `w` workers. In a single pass, he can make `m * w` candies. After
  each pass, he can decide whether to spend some of his candies to buy more
  machines or hire more workers. Buying a machine or hiring a worker costs `p`
  units, and there is no limit to the number of machines he can own or workers
  he can employ.
  Karl wants to minimize the number of passes to obtain the required number of
  candies at the end of a day. Determine that number of passes.

_The optimal strategy involves, at each round, either spending all the "money" (i.e. candles)
on purchasing machines/workers, or saving. When purchasing, one needs to find
an optimal (purchase) allocation to maximise `m * w` (so `m` should be as close to
`w` as possible). At each round `r`, compute the number of rounds required to collect
enough money assuming saving from `r` until the end, and update this minimum 
amount at each round (running min). Instead of using recursion to explore 
two possibilities at each round (buy vs. wait), buy candies each time until the stopping condition
(enough candles) is satisfied or until the running min is smaller than current count 
(this means that at some previous round the optimal strategy was to start saving from 
that round on). In order to avoid timeout, if `p` (price) is bigger than `m * w`, we should
avoid looping and incrementing rounds until we have enough money. We could 
perform a shortcut by calculating the amount of rounds needed to collect 
enough money and update the `count` and money collected accordingly. In case
this waiting time turns out to be too high (i.e. `p` is too big) and we
can collect enough candles to meet the condition before even making `p`, return
the current running min._
  

## Sorting  
 - [x] Sorting: Bubble sort      
 > Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm.  
 - [x] Sorting: Comparator      
 > Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array.  
 - [x] Mark and Toys   
 > Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy?

- [x] Merge Sort: Counting Inversions
> Given `d` datasets, print the number of inversions that must be swapped to sort each dataset on a new line.

_Use Merge Sort_
  
## Stacks and Queues  
 - [x] Stacks: Balanced brackets      
 > Given a string of brackets `{}[]()` state if they are balanced or not.
 
 _Push each bracket on the stack and pop if found the matching one. If closing bracket does not match the one on the top of the stack - Return `False`._    
 - [x] Queues: A tale of two stacks      
> Build a queue using two stacks.  
  
  _There are two methods: 1) make `push` operation costly and 2) make `pop` operation costly._  
 *1) Push operation costly*  
 **`push`**      
 _- while first stack is not empty - put all elements from the first stack on the second one,_      
 _- push the element on the first stack,_      
 _- move all elements back from the second stack to the first one._      
 **`pop`**      
 _- if the first stack is empty - return `Error`,_      
 _- else `pop` the element from the first stack._  
 
  *2) Pop operation costly*  
   **`push`**  
  _- insert an element to the first stack,_      
 **`pop`**      
 _- if both stacks are empty - return `Error`,_      
 _- if second stack is empty - put all elements from the first stack on the second stack,_      
 _- pop the element from the second stack._
 
 - [x] Stacks: A tale of two queues      
> Build a stack using two queues  
  
  _There are again two methods: 1) make `push` operation costly and 2) make `pop` operation costly._  
  _1) Make push operation costly_  
  **`push`**  
  _- enqueue element to second queue,_  
  _- move all elements 
   the first queue to the second one,_  
   _- swap queues' names (to avoid the necessity of moving elements back to the first queue._
   
   _2) Make pop operation costly_  
   **`push`**  
   _- enqueue element to the first queue_  
   **`pop`**  
   _- move all elements (except the last one) from the first queue to the second one,_  
   _- return the remaining element on the first queue,_  
   _- swap queues' names._   


- [x] Castle on the Grid
> You are given a square grid with some cells open (.) and some blocked (X).
Your playing piece can move along any row or column until it reaches the edge
of the grid or a blocked cell. Given a grid, a start and an end position,
determine the number of moves it will take to get to the end position.

_Build an auxiliary method `possible fields` that, given a field, returns
a list of possible fields that the piece can move to. Do a BFS/DFS marking each
visited field. For each possible field store the distance to it from
the beginning. Distance for each field is equal to the incremented distance
to previous field._

- [x] Largest Rectangle
> Maximise a rectangular area under the histogram.

_Use an increasing stack to store the indeces of rectangles.
Good explanation:_
[Stack Overflow](https://stackoverflow.com/questions/4311694/maximize-the-rectangular-area-under-histogram)_

- [x] Min Max Riddle
> Given an integer array of size , find the maximum of the minimum(s) of every
window size in the array. The window size varies from 1 to N.

_For each element (index) in the array, use stack to keep track of the
index of the first element that is smaller. Invoke the function two times:
for given array `a` and its reverse (to know the index of the first element 
that is smaller to the left). Then compute diameters of max windows for 
each element (index) for which this element is the smallest. Keep that
information in the hashmap and at the end iterate through it. Note that
for decreasing window size, the `max` of all of them can be either the same or
higher._

- [x] Poisonous Plants
> You are given the initial values of the pesticide in each of the plants. Print
  the number of days after which no plant dies, i.e. the time after which there
  are no plants with more pesticide content than the plant to their left.
> For example, pesticide levels `p = [3, 6, 2, 7, 5]`. Using a 1-indexed array,
  day 1 plants 2 and 4 die leaving `p = [3, 2, 5]`. On day 2, plant 3 of the current
  array dies leaving `p = [3, 2]`. As there is no plant with a higher concentration of
  pesticide than the one to its left, plants stop dying after day 2.

_First, partition `p` into list of non-increasing stacks, so that we know that
the first element in `stack[i + 1]` is bigger than `stack[i]`. After building such
list we can iteratively remove those first elements from each stack while
removing the empty lists. After each round of `pop`ing the elements we merge 
the neighbouring stacks if they can form a bigger, non increasing stack. In order
to avoid timeout do `stacks[1:] = [s for s in stacks[1:] if len(s) != 1]` to avoid 
expensive removals. Also, use `stack.pop(0)` instead of slicing (i.e. `stack[1:]`)
which requires copying the whole list. Another approach to the problem would be a 
solution similar to the "The Stock Span Problem"._


## String Manipulation  
 - [x] Strings: Making anagrams 
 > How many deletions needed to make two strings anagrams? 
 
_Insert each char from the first string in the dict (char as a `key` and counter as a `value`), then for each char in the second string subtract the counter and count the number of common letters. Then return:      
 `len(str1) + len(str2) - 2 * numCommonLetters`_ 
 
 - [x] Alternating Characters
 > You are given a string containing characters A and B only. Your task is to change it
into a string such that there are no matching adjacent characters. To do this, you
are allowed to delete zero or more characters in the string.

 - [x] Sherlock and the Valid String
 > Sherlock considers a string to be valid if all characters of the string appear the same number of times.
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters
will occur the same number of times. Given a string `s`, determine if it is valid.
If so, return `YES`, otherwise return `NO`.

_Solve using two dictionaries: one for counting letters in the string, the second one for keeping 
information of how many letters (value) appeared at particular frequency (key); e.g.
{3:1, 4:2} means that there is one letter that appears 3 times and two letters that
appear four times._

- [x] Special Palindrome Again
> Find Special palindromic sub-strings in a string

_Build a list of tuples, e.g. for `"monopoo"` -> `[(m,1), (o,1), (n,1), (o,1), (p,1), (o,2)]`.
Then, in first pass, count the number of substrings that have only the same letters. 
Remember that for `n` letters, there is `n(n-1)/2` such substrings. In the second
pass slide a window of size `3`, checking for a pattern, for which the middle tuple
has only a one element._

- [x] Common Child
> A string is said to be a child of a another string if it can be formed by
deleting 0 or more characters from the other string. Given two strings of
equal length, what's the longest string that can be constructed such that it
is a child of both?

_This is essentially a Longest Common Subsequence Problem. Solve it in `O(nm)`
time using Dynamic Programming, where `n` and `m` are lengths of strings.
Construct a 2D array of size `(n+1)(m+1)` and fill zero'th row and column with
zeros (LCS of empty string with anything is zero). Then iterate through each
row and column and compute LCS based on memoized solutions to subproblems._

## Trees  
 - [x] Tree: Height of a Binary Tree 
 - [x] Binary Search Tree: Lowest Common Ancestor
 - [x] Trees: Is this a binary search tree?      
> Check if given tree is a BST.  Assume a node has has attributes: data, left, right 

  _Check recursively with parameters min, max:_ `def isBST(root, min=None, max=None):` _For the right branch set the value of min, for the left branch set the value of max (i.e. nothing in the right branch can be smaller or equal to Min)._      
 _- base case: if not root - Return `True`,_      
 _- if min is not None and `root.data <= min` - Return `False`,_      
 _- if max is not None and `root.data >= max` - Return `False`,_      
 _- check recursively left and the right branches with `root.data` set as max and min respectively._

 - [x] Tree: Huffman Decoding
 > You are given pointer to the root of the Huffman tree and a binary coded string
to decode. You need to print the decoded string.
