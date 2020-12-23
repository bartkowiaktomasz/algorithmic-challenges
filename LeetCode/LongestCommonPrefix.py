from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        if not strs:
            return ""
        try:
            while True:
                char = strs[0][i]
                if all(s[i] == char for s in strs):
                    i += 1
                else:
                    break
        except IndexError:
            return strs[0][:i]
        return strs[0][:i]

sol = Solution()
strs_list = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"]
]
print(
    [sol.longestCommonPrefix(strs) for strs in strs_list]
)
