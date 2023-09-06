from collections import deque

class StackElement:
    def __init__(self, val, min):
        self.val = val
        # For a given element, indicates the minimum of the stack below it
        #  (and including it)
        self.min = min

class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()

    def push(self, val: int) -> None:
        minimum = min(val, self.stack[-1].min if self.stack else float('inf'))
        elem = StackElement(val, minimum)
        self.stack.append(elem)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min