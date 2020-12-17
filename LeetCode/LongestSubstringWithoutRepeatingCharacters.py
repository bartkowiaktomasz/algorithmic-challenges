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
        letters_to_idx = dict()
        length_longest_substr = 0
        i = 0
        for j, c in enumerate(s):
            if c not in letters_to_idx:
                letters_to_idx[c] = j
            else:
                duplicate_idx = letters_to_idx[c]
                i = max(duplicate_idx + 1, i)
                letters_to_idx[c] = j
            length_longest_substr = max(length_longest_substr, j - i + 1)

        return length_longest_substr

input1 = "abba"
print(
    Solution().lengthOfLongestSubstring(input1)
)
