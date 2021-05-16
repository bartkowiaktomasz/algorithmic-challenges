import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        arr = [True for _ in range(n)]
        arr[0], arr[1] = False, False
        for m in range(2, int(n ** 0.5) + 1):
            i = m * m
            while i < n:
                arr[i] = False
                i += m
        return sum(arr)  # sum of the values == True

sol = Solution()
print(
    sol.countPrimes(10)
)