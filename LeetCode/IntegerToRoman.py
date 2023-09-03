from typing import List


class Solution:
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    def intToRoman(self, num: int) -> str:
        out, i = [], 0
        while num:
            s = num // self.values[i] * self.numerals[i]
            if s: out.append(s)
            num = num % self.values[i]
            i += 1
        return ''.join(out)

sol = Solution()
print(
    sol.intToRoman(1994)
)