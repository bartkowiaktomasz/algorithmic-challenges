from typing import List


class Solution:
    def __init__(self):
        self.answer = [0 for _ in range(int(10e4))]
        for i in range(1, int(10e4) + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    self.answer[i - 1] = "FizzBuzz"
                else:
                    self.answer[i - 1] = "Fizz"
            elif i % 5 == 0:
                if i % 3 == 0:
                    self.answer[i - 1] = "Fizz"
                else:
                    self.answer[i - 1] = "Buzz"
            else:
                self.answer[i - 1] = str(i)

    def fizzBuzz(self, n: int) -> List[str]:
        return self.answer[:n]

sol = Solution()
print(
    sol.fizzBuzz(15)
)