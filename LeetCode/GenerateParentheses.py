import copy
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generateParenthesisRec(n: int, left: int, right: int, s: List):
            if left > n or right > n:
                return
            if left == n and right == n:
                res.append("".join(s))
                return
            if right > left:
                return
            s2 = copy.copy(s)
            s2.extend(')')
            s.extend('(')
            generateParenthesisRec(n, left + 1, right, s)
            generateParenthesisRec(n, left, right + 1, s2)
        generateParenthesisRec(n, 0, 0, s=[])
        return res

s = Solution()
print(
    s.generateParenthesis(3)
)
