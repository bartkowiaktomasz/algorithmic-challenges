from typing import List


class Solution:
    _alphabet = "abcdefghijklmnopqrstuvwxyz"
    keyboard = {
        "2": _alphabet[0:3],
        "3": _alphabet[3:6],
        "4": _alphabet[6:9],
        "5": _alphabet[9:12],
        "6": _alphabet[12:15],
        "7": _alphabet[15:19],
        "8": _alphabet[19:22],
        "9": _alphabet[22:26],
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(self.keyboard[digits[0]])
        else:
            prev = self.letterCombinations(digits[:-1])
            letters = list(self.keyboard[digits[-1]])
            return [e + l for e in prev for l in letters]


s = Solution()
digits_l = [
    "",
    "2",
    "23"
]
print(
    [s.letterCombinations(digits) for digits in digits_l]
)
