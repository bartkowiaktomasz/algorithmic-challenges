from typing import List


class Solution:
    def split_pattern(self, p: str) -> List[str]:
        pattern_len = len(p)
        i = 0
        patterns = []
        while i < pattern_len:
            if p[i].isalpha() or p[i] == ".":
                if i + 1 < pattern_len:
                    if p[i + 1] == "*":
                        patterns.append(p[i] + "*")
                        i += 1
                else:
                    patterns.append(p[i])
            i += 1
        return patterns

    def is_match_single_pattern(self, s, p):
        pattern_len = len(p)
        if pattern_len == 1:


    def isMatch(self, s: str, p: str) -> bool:
        split_pattern = self.split_pattern(p)
        for p in split_pattern:
            if not self.is_match_single_pattern(s, p):
                return False
        return True


s = Solution()
x = [
    "a",
    "a*",
    ".*",
    "c*a*b",
    "mis*is*p*."
]

print(
    list(map(s.split_pattern, x))
)
