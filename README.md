# Crack the coding interview - algorithm questions solutions

## Hackerrank
Solutions to questions taken from _Hackerrank - Cracking the Coding Interview Challenges_.

### Data Structures
 - [x] Arrays: Left rotation  
 - [x] Strings: Making anagrams  
 _**How many deletions needed to make two strings anagrams?**_  
 _- Insert each char from the first string in the dict (char as a `key` and counter as a `value`), then for each char in the second string subtract the counter and count the number of common letters. Then return:  
 `len(str1) + len(str2) - 2 * numCommonLetters`_
 - [x] Hash tables: Ransom note  
 **_Given the words in the magazine and the words in the ransom note, print `Yes` if he can replicate his ransom note _exactly_ using whole words from the magazine; otherwise, print `No`._**  
 _- Insert each word from `magazine` to a dict (char as a `key` and counter as a `value`) and then, for each word in `ransom note` check if the word it is available._  
 - [ ] Linked Lists: Detect a cycle  
 _**Given a linked list detect if it contains a cycle.**_  
 _- Use Floyd's cycle detection algorithm - create two pointers, one (slow) jumping from list to the next node, the second one (quick) jumping to every 2nd node. If they eventually meet, there is a loop._


### Algorithms
 - [x] Sorting: Bubble sort  
 - [x] Sorting: Comparator  
 - [x] Hash Tables: Ice cream parlor  
_**Given list of integers, find two of them that sum to n.**_  
_- Iterate through the list once and add each value to the dict if it does not already contain an element that, when added, gives a sum of n._
 - [x] Stacks: Balanced brackets  
 _**Given a string of brackets `{}[]()` state if they are balanced or not**_  
 _- Push each bracket on the stack and pop if found the matching one. If closing bracket does not match the one on the top of the stack - Return `False`._  
 - [x] Queues: A tale of two stacks  
 _**Build a queue using two stacks.**_  
 _There are two methods: 1) make `push` operation costly and 2) make `pop` operation costly._  
 _1) Push operation costly_  
 **`push`**  
 _- while first stack is not empty - put all elements from the first stack on the second one,_  
 _- push the element on the first stack,_  
 _- move all elements back from the second stack to the first one._  
 **`pop`**  
 _- if the first stack is empty - return `Error`,_  
 _- else `pop` the element from the first stack._  
_2) Pop operation costly_  
**`push`**  
_- insert an element to the first stack,_  
 **`pop`**  
 _- if both stacks are empty - return `Error`,_  
 _- if second stack is empty - put all elements from the first stack on the second stack,_  
 _- pop the element from the second stack._  
 _**Build a stack using two queues**_  
_There are again two methods: 1) make `push` operation costly and 2) make `pop` operation costly._  
_1) Make push operation costly_  
**`push`**  
_- enqueue element to second queue,_  
_- move all elements from the first queue to the second one,_  
_- swap queues' names (to avoid the necessity of moving elements back to the first queue._  
_2) Make pop operation costly_  
**`push`**  
_- enqueue element to the first queue_  
**`pop`**  
_- move all elements (except the last one) from the first queue to the second one,_  
_- return the remaining element on the first queue,_  
_- swap queues' names._  

 - [x] Trees: Is this a binary search tree?  
 **_Check if given tree is a BST.  Assume a node has has attributes: data, left, right _**  
 _- check recursively with parameters min, max:_  
`def isBST(root, min=None, max=None):`  
_For the right branch set the value of min, for the left branch set the value of max (i.e. nothing in the right branch can be smaller or equal to Min)._  
 _- base case: if not root - Return `True`,_  
 _- if min is not None and `root.data <= min` - Return `False`,_  
 _- if max is not None and `root.data >= max` - Return `False`,_  
 _- check recursively left and the right branches with `root.data` set as max and min respectively._  
