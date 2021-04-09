from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        current = []; quantifier = []
        for c in s:
            if c.isalpha():
                current.append(c)
            elif c.isdigit():
                quantifier.append(c)
            elif c == '[':
                # current must have a quantifier, e.g. ["2", "3"], i.e. 23
                k = int("".join(quantifier))
                stack.append((current, k))
                current = []; quantifier = []
            else:  # c == ']'
                previous, k = stack.pop()
                current = previous + current * k
        return "".join(current)


sol = Solution()
s = "abc3[cd]xyz"
print(
    sol.decodeString(s)
)