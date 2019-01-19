"""
Complete the function isBalanced in the editor below.
It must return a string: YES if the sequence is balanced or NO if it is not.
"""

import os
from collections import deque

def isOpening(bracket):
    if bracket == '(' or bracket == '{' or bracket == '[':
        return True
    else:
        return False


def areMatching(a, b):
    if a == '(' and b == ')' or a == '{' and b == '}' or a == '[' and b == ']':
        return True
    else:
        return False


# Complete the isBalanced function below.
def isBalanced(s):
    queue = deque()
    for bracket in s:
        if isOpening(bracket):
            queue.append(bracket)
        else:
            try:
                element = queue.pop()
            except:
                return "NO"
            if not areMatching(element, bracket):
                return "NO"

    if len(queue) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()
