from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        cur, sign, n = 0, 1, 0  # initialise "n" in case expression starts with "-"
        stack = []
        i =  0
        while i < len(s):
            if s[i].isdigit():
                n = 10 * n + int(s[i])  # Nifty trick to capture non-single-digit numbers
            elif s[i] in ["+", "-"]:
                cur += sign * n
                sign = 1 if s[i] == "+" else -1
                n = 0
            elif s[i] == "(":
                # save progress. "cur" is our current answer
                # "sign" will be used to prepend to the result of next evaluation 
                stack.append([cur, sign])
                cur, sign, n = 0, 1, 0
            elif s[i] == ")":
                prev, prev_sign = stack.pop()
                cur = prev + prev_sign * (cur + sign * n)
                sign, n = 1, 0
            else: pass  # ' ' is ignored
            i += 1
        cur += sign * n  # boundary condition - we might have non-zero "n"
        return cur

# " 2-(1+1) + 2 "
# " 2-1 + 2 "
sol = Solution()
print(
    sol.calculate(" 1+1+-1+1 ")
)