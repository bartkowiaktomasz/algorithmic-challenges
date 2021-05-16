class Solution:
    def transform(self, n: int) -> int:
        """
        Transform as per rules (sum of squares of each digit)
        e.g. 19 -> 1^2 + 9^2 = 82
        """
        sum_ = 0
        while n != 0:
            last_digit = n % 10
            sum_ += pow(last_digit, 2)
            n //= 10
        return sum_
        
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        slow = n
        fast = self.transform(n)
        while slow != fast:
            slow = self.transform(slow)
            fast = self.transform(self.transform(fast))
            if fast == 1:
                return True
        return False
        
sol = Solution()
print(
    sol.isHappy(2)
)