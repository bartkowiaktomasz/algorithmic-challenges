class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(
            [i for i in [w.strip() for w in s.strip().split(" ")][::-1] if i]
        )

sol = Solution()
s = "the sky    is blue"
print(
    sol.reverseWords(s)
)