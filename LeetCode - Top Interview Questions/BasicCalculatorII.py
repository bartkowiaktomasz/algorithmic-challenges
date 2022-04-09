"""
Given a string `s` which represents an expression, evaluate this
expression and return its value. 

The integer division should truncate toward zero

Examples:
--------
Input: s = "3+2*2"
Output: 7
"""

from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")  # remove whitespaces
        stack = deque()
        i = 0
        cur = ""
        while i < len(s):
            while i < len(s) and s[i] not in {"+", "-", "*", "/"}:
                cur += s[i]
                i += 1
            stack.append(int(cur))
            if i == len(s):
                break
            stack.append(s[i])
            cur = ""
            i += 1
        # 10 / 5 + 2
        res = 0
        while stack:
            if len(stack) == 1:
                res += stack[0]
                break
            a = stack.popleft()
            op = stack.popleft()
            b = stack.popleft()
            if op == "*":
                stack.appendleft(a * b)
            elif op == "/":
                stack.appendleft(int(a / b))
            elif op == "+":
                res += a
                stack.appendleft(b)
            else:
                res += a
                stack.appendleft(-b)
        return res


sol = Solution()
# input1 = "3+2*2"
# expected1 = 7
# assert sol.calculate(input1) == expected1

# input2 = " 3/2 "
# expected2 = 1
# assert sol.calculate(input2) == expected2

# input3 = " 3+5 / 2 "
# expected3 = 5
# assert sol.calculate(input3) == expected3

# input4 = "1-1-1"
# expected4 = -1
# assert sol.calculate(input4) == expected4

# input5 = "1-1+1"
# expected5 = 1
# assert sol.calculate(input5) == expected5

# input6 = "14/3/2"
# expected6 = 2
# assert sol.calculate(input6) == expected6

# input7 = "1+2*5/3+6/4*2"
# expected7 = 6
# assert sol.calculate(input7) == expected7

input8 = "14-3/2"
expected8 = 13
assert sol.calculate(input8) == expected8
