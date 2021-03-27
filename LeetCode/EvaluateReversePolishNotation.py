from typing import List

class Solution:
    OPS = ["+", "-", "*", "/"]
    
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        def solve(a: int, b: int, op: str, tokens: List[str]):
            if a is not None and b is not None and op is not None:
                res = self.evaluate(a, b, op)
                return res
            elem = tokens.pop()
            if elem in self.OPS:
                if b is not None:
                    a = solve(None, None, elem, tokens)
                    return solve(a, b, op, tokens)
                elif op is not None:
                    b = solve(None, None, elem, tokens)
                    return solve(None, b, op, tokens)
                else:
                    return solve(None, None, elem, tokens)
            else:
                if b is not None:
                    # elem is a number so it's "a"
                    return solve(float(elem), b, op, tokens)
                else:
                    # elem is a number so it's "b"
                    return solve(None, float(elem), op, tokens)
        return int(solve(None, None, None, tokens))
    
    def evaluate(self, a: int, b: int, op: str):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        else:  # op == "/"
            return int(a / b)

tokens = ["8"]
sol = Solution()
print(
    sol.evalRPN(tokens)
)