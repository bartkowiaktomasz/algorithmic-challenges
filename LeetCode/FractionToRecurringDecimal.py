class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(int(numerator / denominator))
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        reminders = dict()  # reminder -> idx
        quotient, rem = numerator // denominator, numerator % denominator
        reminders[rem] = 0
        res_prefix, res_suffix = [sign + str(quotient) + "."], []
        numerator = rem * 10
        i = 1
        while True:
            quotient, rem = numerator // denominator, numerator % denominator
            res_suffix.append(str(quotient))
            if rem == 0:
                return "".join(res_prefix + res_suffix)
            elif rem in reminders:
                return "".join(res_prefix + res_suffix[:reminders[rem]] + ["("] + res_suffix[reminders[rem]:] + [")"])
            else:
                reminders[rem] = i
            numerator = rem * 10
            i += 1
        return "".join(res_prefix + res_suffix)


sol = Solution()
numerator = 1
denominator = 6
print(
    sol.fractionToDecimal(numerator, denominator)
)
