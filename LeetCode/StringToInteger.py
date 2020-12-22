MAXINT = pow(2, 31) - 1
MININT = -pow(2, 31)


class Solution:
    def lstrip(self, s, split):
        if not s:
            return s
        i = 0
        for c in s:
            if c == split:
                i += 1
            else:
                break
        return s[i:]

    def myAtoi(self, s: str) -> int:
        s = self.lstrip(s, split=" ")
        if not s or (not s[0].isdigit() and s[0] not in ["-", "+"]):
            return 0
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        else:
            sign = 1
        result = 0
        for char in s:
            if not char.isdigit():
                break
            digit = ord(char) - ord("0")
            if (result > MAXINT // 10) or (result == (MAXINT // 10) and digit > 7):
                if sign == -1:
                    return MININT
                else:
                    return MAXINT
            result = digit + result * 10
        return sign * result


s = Solution()
x = [
    "42",
    "4193 with words",
    "words and 987",
    "-91283472332",
    "-42",
    "",
    "-",
    "+1",
    "++1"
]

print(
    list(map(s.myAtoi, x))
)
