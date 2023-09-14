class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x > 0 and x % 10 == 0): return False
        rev_x = 0
        while rev_x < x:
            rev_x = (rev_x * 10) + (x % 10)
            x //= 10
        return (rev_x == x) or (x == rev_x // 10)