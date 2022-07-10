from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def solve(s: str, k: int):
            if not s:
                return 0
            c = Counter(s)
            least_freq_elem = min(c, key=c.get)
            least_freq = c[least_freq_elem]
            if least_freq >= k:
                return len(s)
            else:
                return max([solve(subs, k) for subs in s.split(least_freq_elem)])
        return solve(s, k)


sol = Solution()
print(
    sol.longestSubstring(
        s = "ababbc", k = 2
    )
)