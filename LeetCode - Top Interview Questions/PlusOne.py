from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)):
            j = len(digits) - 1 - i
            d = digits[j]
            digits[j] = (d + carry) % 10
            carry = (d + carry) // 10
        if carry == 0:
            return digits
        else:
            return [carry] + digits

s = Solution()
digits = [9, 8, 9]
print(
    s.plusOne(digits)
)