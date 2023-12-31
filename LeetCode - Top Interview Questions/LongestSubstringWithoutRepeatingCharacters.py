"""
Given a string s, find the length of the longest substring without repeating characters.

e.g.
"abcabcbb" -> 3
"bbbbb" -> 1
"pwwkew" -> 3
"abba" -> 2
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        i, j, max_l = 0, 1, 1
        seen = set([s[i]])
        while j < len(s):
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                j += 1
            max_l = max(max_l, j - i)
            if i == len(s) or j == len(s): return max_l
            while s[i] != s[j]:
                seen.remove(s[i])
                i += 1
            seen.remove(s[i])
            i += 1
        return max_l

input1 = "abba"
print(
    Solution().lengthOfLongestSubstring(input1)
)
