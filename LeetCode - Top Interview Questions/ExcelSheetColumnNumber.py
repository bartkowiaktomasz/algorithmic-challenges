class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        pos, res = 0, 0
        for char in columnTitle[::-1]:
            res += (ord(char) - 64) * pow(26, pos)
            pos += 1
        return res
        
sol = Solution()
columnTitle = "FXSHRXW"
print(
    sol.titleToNumber(columnTitle)
)