"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome_len = 0
        max_palindrome = ''
        for i, c in enumerate(s):
            # For each letter (at index i) start expanding substring to find max
            #  palindrome
            d = 0
            while i - d >= 0 and i + d < len(s):
                # Case when substring has odd len
                if s[i - d] == s[i + d]:
                    palindrome_len = 2 * d + 1
                    palindrome = s[i - d: i + d + 1]
                    if palindrome_len > max_palindrome_len:
                        max_palindrome_len = palindrome_len
                        max_palindrome = palindrome
                    d += 1
                else:
                    break
        for i, c in enumerate(s):
            # For each pair of letters (index i, i+1) start expanding substring to
            #  find max palindrome
            d = 0
            while i - d >= 0 and i + 1 + d < len(s):
                # Case when substring has even len
                if s[i - d] == s[i + 1 + d]:
                    palindrome_len = 2 * d + 2
                    palindrome = s[i - d: i + d + 2]
                    if palindrome_len > max_palindrome_len:
                        max_palindrome_len = palindrome_len
                        max_palindrome = palindrome
                    d += 1
                else:
                    break
        return max_palindrome


s = Solution()
s1 = "babad"
s2 = "cbbd"
s3 = "a"
s4 = "ac"

print(
    s.longestPalindrome(s4)
)
