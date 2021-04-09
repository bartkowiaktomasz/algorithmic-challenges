from typing import List
import copy

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[None for _ in range(n)] for _ in range(n)]
        
        def is_palindrome(dp: List[List[int]], s: str, i: int, j: int):
            if dp[i][j] is not None:
                return dp[i][j]
            if j <= i:
                return True
            if s[i] == s[j] and is_palindrome(dp, s, i + 1, j - 1):
                dp[i][j] = True
                return True
            dp[i][j] = False
            return False
        
        res = []
        def solve(single_res: List[str],  i: int, j: int):
            if j == n:
                if i == n:
                    res.append(single_res)
            else:
                if is_palindrome(dp, s, i, j):
                    single_res_cp = copy.copy(single_res)
                    single_res_cp_2 = copy.copy(single_res)
                    single_res_cp.append(s[i:j + 1])
                    solve(single_res_cp, j + 1, j + 1)
                    solve(single_res_cp_2, i, j + 1)
                else:
                    single_res_cp = copy.copy(single_res)
                    solve(single_res_cp, i, j + 1)
        solve([], 0, 0)
        return res

s = "efe"
sol = Solution()
print(
    sol.partition(s)
)