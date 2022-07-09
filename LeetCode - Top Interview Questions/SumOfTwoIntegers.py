class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        # Solution if both a, b are positive:

        res, carry = a ^ b, (a & b) << 1 
        while carry != 0:
            prev_carry = carry
            carry = (carry & res) << 1
            res = res ^ prev_carry
        return res

        # Otherwise need to handle infinite loop for e.g.
        # a = -1, b = 1
        """
        mask = 0xFFFFFFFF
        max_ = 0x7FFFFFFF
        res, carry = (a ^ b) & mask, ((a & b) << 1) & mask 
        while carry != 0:
            prev_carry = carry
            carry = ((carry & res) << 1) & mask
            res = (res ^ prev_carry) & mask
        return res if res <= max_ else ~(res ^ mask)

sol = Solution()
print(
    sol.getSum(-12,-8)
)