class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Given two integers `left` and `right` that represent the range [left, right],
        return the bitwise AND of all numbers in this range, inclusive.

        This is equivalent to finding the largest common prefix between left and right
        That's because all bits to the right of the common prefix are the ones
        that swap 0 <-> 1 for some number between `left` and `right`.
        """
        n_bits = 32
        left_bin = str(bin(left))[2:].rjust(n_bits, '0')  # e.g. 5 -> 00000101
        right_bin = str(bin(right))[2:].rjust(n_bits, '0')
        i = 0
        while i < len(left_bin) and left_bin[i] == right_bin[i]: i += 1
        res_bin = left_bin[:i] + "0" * (n_bits - i)
        return int(res_bin, 2)  # '00000101` -> 5
    

sol = Solution()
print(
    sol.rangeBitwiseAnd(5, 7)
)
