class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        lookup_double_char = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        i = 0
        sum = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:(i+1) + 1] in lookup_double_char:
               sum += lookup_double_char[s[i:(i+1) + 1]]
               i += 2
            else:
                sum += lookup[s[i]]
                i += 1
        return sum

sol = Solution()
s_list = [
    "III", "IV", "IX", "LVIII", "MCMXCIV"
]
print(
    [sol.romanToInt(s) for s in s_list]
)
