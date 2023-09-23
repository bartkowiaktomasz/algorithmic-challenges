class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_ = {}
        map_vals = set()
        for i in range(len(s)):
            if s[i] in map_:
                if map_[s[i]] == t[i]: i += 1
                else: return False
            else:
                if t[i] in map_vals: return False
                else: map_[s[i]] = t[i]; map_vals.add(t[i]); i += 1
        return True

s = "egg"; t = "add"
sol = Solution()
print(
    sol.isIsomorphic(s, t)
)