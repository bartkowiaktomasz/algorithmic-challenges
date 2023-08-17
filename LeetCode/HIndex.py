from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_citations = max(citations)
        # counting sort
        cit_cnts = [0 for _ in range(max_citations + 1)]
        for c in citations: cit_cnts[c] += 1
        # reversed cumsum
        # e.g. [1,1,0,1,0,1,1] -> [5,4,3,3,2,2,1]
        for i in range(len(cit_cnts) - 2, -1, -1): cit_cnts[i] += cit_cnts[i + 1]
        for i in range(len(cit_cnts) -1, -1, -1):
            if i <= cit_cnts[i]: return i

sol = Solution()
print(
    sol.hIndex([1,3,1])
)