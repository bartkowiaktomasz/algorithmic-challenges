"""
The count-and-say sequence is a sequence of digit strings defined by the recursive
formula:

`countAndSay(1) = "1"`
`countAndSay(n)` is the way you would "say" the digit string from
`countAndSay(n-1)`, which is then converted into a different digit string.
"""
from itertools import groupby


class Solution:
    def countAndSayIter(self, s: str):
        """
        Single iteration of countAndSay
        e.g. countAndSayIter("111223") = "312213"
        """
        groups = ["".join(grp) for _, grp in groupby(s)]
        out = []
        for g in groups:
            out.append(str(len(g)) + g[0])
        return "".join(out)

    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(1, n):
           s = self.countAndSayIter(s)
        return s


sol = Solution()
s = "111223"
print(
    sol.countAndSay(4)
)
