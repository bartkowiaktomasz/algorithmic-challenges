"""
Given two strings `s` and `t`, return the minimum window in `s` which will 
contain all the characters in `t`. If there is no such window in `s` that covers 
all characters in `t`, return the empty string `""`. Note: `t` can contain
duplicates and the output window needs to contain all of them.
"""

from collections import Counter, defaultdict
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        low, high = 0, 0
        count_t = Counter(t)
        # Remove letters from this counter when building the first valid window
        #  i.e. when shifting `high` initially to the right
        chars_t_remaining_to_see = Counter(t)
        count_window = Counter()
        min_window_size, min_window_low = sys.maxsize, -1
        while high < len(s):
            char = s[high]
            count_window[char] += 1
            if chars_t_remaining_to_see[char] > 1:
                chars_t_remaining_to_see[char] -= 1
            else:
                del chars_t_remaining_to_see[char]

            if not chars_t_remaining_to_see:
                # Window has all needed chars
                char = s[low]
                while count_window[char] > count_t[char]:
                    low += 1
                    count_window[char] -= 1
                    char = s[low]
                window_size = high - low + 1
                if window_size > 0 and window_size < min_window_size:
                    min_window_size, min_window_low = window_size, low
                if min_window_size == len(t):
                    break
            high += 1
        if chars_t_remaining_to_see:
            return ""
        return s[min_window_low : min_window_low + min_window_size]


s = "cabwefgewcwaefgcf"
t = "cae"

sol = Solution()
print(sol.minWindow(s, t))

