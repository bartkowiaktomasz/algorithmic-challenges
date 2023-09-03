class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s and not t: return True
        if s and not t: return False
        if t and not s: return True
        i, j = 0, 0
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
            if i == len(s): return True
        return False

sol = Solution()
print(
    sol.isSubsequence("abc", "ahbgdc")
)