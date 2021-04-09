class Solution:
    def reverseBits(self, n: int) -> int:
        i, res, NUM_BITS = 0, 0, 32
        while i < NUM_BITS:
            # Get the least significant digit of n
            bit = 1 & n
            # Shift the bit to the correct position and set the bit in the result
            #  with OR
            res |= (bit << (NUM_BITS - 1 - i))
            i += 1
            # Shift n to allow to retrieve the next siginificant digit in the
            #  next iteration
            n = n >> 1
        return res


n = 3
sol = Solution()
print(
    sol.reverseBits(n)
)