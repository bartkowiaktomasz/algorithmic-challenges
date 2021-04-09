class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square == x:
                return mid
            if square < x:
                low = mid + 1
            else:
                high = mid - 1
        return min(low, high)


s = Solution()
[print(s.mySqrt(i)) for i in range(20)]