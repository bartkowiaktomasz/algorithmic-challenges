
# HackeRank Questions  
Solutions to selected questions taken from _Hackerrank - Cracking the Coding Interview Challenges_ and _HackerRank - Interview Preparation Kit_.    
  
## Arrays  
 - [x] 2D Array - DS  
 - [x] Arrays: Left rotation  
 > A _left rotation_ operation on an array shifts each of the array's elements unit to the left.
 - [x] New Year Chaos  
 - [x] Minimum Swaps 2  
 > You need to find the minimum number of swaps required to sort the array in ascending order.   
 - [x] Array Manipulation

## Dictionaries and Hashmaps  
- [x] Hash Tables: Ransom Note
> Given the words in the magazine and the words in the ransom note, print `Yes` if he can replicate his ransom note _exactly_ using whole words from the magazine; otherwise, print `No`.

- [x] Two Strings
> Given two strings, determine if they share a common substring. A substring may be as small as one character.
 
## Greedy Algorithms 
- [x] Minimum Absolute Difference in an Array
> Given an array of integers, find and print the minimum absolute difference between any two elements in the array.

- [x] Luck Balance

## Linked Lists  
- [x] Linked Lists: Detect a cycle      
> Given a linked list detect if it contains a cycle.

 _Use Floyd's cycle detection algorithm - create two pointers, one (slow) jumping from list to the next node, the second one (quick) jumping to every 2nd node. If they eventually meet, there is a loop._    

- [x] Inserting a Node Into a Sorted Doubly Linked List  
> Given a reference to the head of a doubly-linked list and an integer, `data`, create a new DoublyLinkedListNode object  
having data value `data` and insert it into a sorted linked list while maintaining the sort.

- [x] Reverse a doubly linked list   
> You’re given the pointer to the head node of a doubly linked list. Reverse the order of the nodes in the list.

 ## Dictionaries and Hashmaps    
- [x] Two Strings    
 > Given two strings, determine if they share a common substring. A substring may be as small as one character.

_It is enough to check if strings share at least one common letter._
  
 - [x] Hash tables: Ransom note      
 > Given the words in the magazine and the words in the ransom note, print `Yes` if he can replicate his ransom note _exactly_ using whole words from the magazine; otherwise, print `No`.
 > 
 _Insert each word from `magazine` to a dict (char as a `key` and counter as a `value`) and then, for each word in `ransom note` check if the word is available._   


## Graphs
 - [x] BFS: Shortest Reach in a Graph
 - [x] DFS: Connected Cell in a Grid

## Miscellaneous  
 - [x] Bit Manipulation: Lonely Integer
 - [x] Time Complexity: Primality

## Recursion and Backtracking
 - [x] Recursion: Fibonacci Numbers
 > Implement Fibonacci sequence recursively.
 - [x] Recursion: Davids' Staircase
 > Complete the  _stepPerms_  function in the editor below. It should recursively calculate and return the integer number of ways Davis can climb the staircase, modulo 10000000007.

## Search  
 - [x] Hash Tables: Ice cream parlor      
> Given list of integers, find two of them that sum to n.  
  
_Iterate through the list once and add each value to the dict if it does not already contain an element that, when added, gives a sum of n._   


## Sorting  
 - [x] Sorting: Bubble sort      
 > Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm.  
 - [x] Sorting: Comparator      
 > Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array.  
 - [x] Mark and Toys   
>Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy?

- [x] Merge Sort: Counting Inversions
> Given `d` datasets, print the number of inversions that must be swapped to sort each dataset on a new line.

_Use Merge Sort_
  
## Stacks and Queues  
 - [x] Stacks: Balanced brackets      
 > Given a string of brackets `{}[]()` state if they are balanced or not  _Push each bracket on the stack and pop if found the matching one. If closing bracket does not match the one on the top of the stack - Return `False`._    
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
  
_2) Pop operation costly_ **`push`** _- insert an element to the first stack,_      
 **`pop`**      
 _- if both stacks are empty - return `Error`,_      
 _- if second stack is empty - put all elements from the first stack on the second stack,_      
 _- pop the element from the second stack._   
 - [x] Stacks: A tale of two queues      
>Build a stack using two queues  
  
  _There are again two methods: 1) make `push` operation costly and 2) make `pop` operation costly._ _1) Make push operation costly_ **`push`** _- enqueue element to second queue,_ _- move all elements from the first queue to the second one,_ _- swap queues' names (to avoid the necessity of moving elements back to the first queue._ _2) Make pop operation costly_ **`push`** _- enqueue element to the first queue_ **`pop`** _- move all elements (except the last one) from the first queue to the second one,_ _- return the remaining element on the first queue,_ _- swap queues' names._   


## String Manipulation  
 - [x] Strings: Making anagrams 
 > How many deletions needed to make two strings anagrams?  
_Insert each char from the first string in the dict (char as a `key` and counter as a `value`), then for each char in the second string subtract the counter and count the number of common letters. Then return:      
 `len(str1) + len(str2) - 2 * numCommonLetters`_   


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