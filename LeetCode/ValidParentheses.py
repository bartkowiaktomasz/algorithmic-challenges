from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")": "(", "}": "{", "]": "["
        }
        open_brackets = mapping.values()
        stack = deque()
        # Optimisation
        if len(s) % 2 != 0:
            return False
        for c in s:
            if c in open_brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                if mapping[c] == stack.pop():
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


s = Solution()
print(
    s.isValid("[")
)
