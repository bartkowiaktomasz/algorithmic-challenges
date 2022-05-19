# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List
from collections import deque

class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> List["NestedInteger"]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: List["NestedInteger"]):
        self.nestedList = deque(nestedList)
    
    def next(self) -> int:
        while not self.nestedList[0].isInteger():
            first = self.nestedList.popleft()
            _queue = deque()
            for elem in first.getList()[::-1]:
                self.nestedList.appendleft(elem)
        return self.nestedList.popleft()
    
    def hasNext(self) -> bool:
         return bool(self.nestedList)

# Your NestedIterator object will be instantiated and called as such:
nestedList = [[]]
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

i = NestedIterator(nestedList)
res = []
while i.hasNext():
     res.append(i.next())
print(res)