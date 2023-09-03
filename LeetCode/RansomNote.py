from typing import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1, c2 = Counter(magazine), Counter(ransomNote)
        return c1 & c2 == c2