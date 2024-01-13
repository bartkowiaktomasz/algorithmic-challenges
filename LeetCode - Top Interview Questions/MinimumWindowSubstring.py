"""
Given two strings `s` and `t`, return the minimum window in `s` which will 
contain all the characters in `t`. If there is no such window in `s` that covers 
all characters in `t`, return the empty string `""`. Note: `t` can contain
duplicates and the output window needs to contain all of them.
"""

from typing import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = j = best_i = best_j = 0
        need, count_need = Counter(t), len(set(t))
        for j, char in enumerate(s, 1):
            need[char] += -1
            if need[char] == 0:
                count_need += -1
            while count_need == 0:
                if best_j == 0 or j - i < best_j - best_i:
                    best_i, best_j = i, j
                need[s[i]] += 1
                if need[s[i]] > 0:
                    count_need += 1
                i += 1
        return s[best_i:best_j]

sol = Solution()
s1, t1 = "aa", "aa"
s2, t2 = "a", "aa"
s3, t3 = "ADOBECODEBANC", "ABC"
s4, t4 = "a", "a"
print(
    sol.minWindow(s1, t1)
)