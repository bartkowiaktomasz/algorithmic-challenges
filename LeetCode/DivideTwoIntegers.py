
class Solution:
    MAX_INT = pow(2, 31) - 1
    MIN_INT = -pow(2, 31)

    def is_overflow(self, sign: int, res: int, i: int):
        if sign == 1 and res > Solution.MAX_INT - (1 << (i - 1)):
            return True
        elif sign == -1 and res > abs(Solution.MIN_INT - 1) - (1 << (i - 1)) + 1:
            return True
        else:
            return False

    def divide(self, dividend: int, divisor: int) -> int:
        """divisor != 0 is given"""
        sign = (dividend < 0) is (divisor < 0)
        sign = 1 if sign else -1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            i = 0
            while dividend >= (divisor << i):
                i += 1
            if i == 0:
                return sign * res
            dividend -= (divisor << (i - 1))
            if self.is_overflow(sign, res, i):
                return Solution.MAX_INT
            res += (1 << (i - 1))
        return sign * res


s = Solution()
print(
    s.divide(22, 3)
)
