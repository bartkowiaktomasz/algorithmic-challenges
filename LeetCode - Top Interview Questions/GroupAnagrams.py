"""
Given an array of strings `strs`, group the anagrams together. You can return 
the answer in any order.
"""

from typing import List, Tuple
from collections import defaultdict


class Solution:
    _ALPHABET_SIZE = 26
    def getCountTuple(self, s: str) -> Tuple[int]:
        count = [0 for _ in range(self._ALPHABET_SIZE)]
        for c in s:
            count[ord(c) - ord('a')] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_strs_map = defaultdict(list)
        for s in strs:
            count = self.getCountTuple(s)
            count_strs_map[count].append(s)
        return list(count_strs_map.values())


s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]

print(
    s.groupAnagrams(strs)
)