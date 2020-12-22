"""
Given a 32-bit signed integer, reverse digits of an integer.
"""
MAXINT = pow(2, 31) - 1
MININT = -pow(2, 31)


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x *= sign

        result = 0
        while x != 0 and x != -1:
            digit = x % 10
            if (result > MAXINT // 10) or (result == (MAXINT // 10) and digit > 7):
                return 0
            result = digit + result * 10
            x = x // 10
        result *= sign
        return result


s = Solution()
i1 = 123
i2 = -123
i3 = 120
i4 = 0
i5 = 1
i6 = 1534236469  # should overflow
print(
    s.reverse(i6)
)
