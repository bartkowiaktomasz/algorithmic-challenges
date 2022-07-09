from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def num_elems_leq_than(x: int):
            nonlocal matrix
            r, c = 0, len(matrix[0]) - 1
            count = 0
            while r < len(matrix) and c >= 0:
                if matrix[r][c] <= x:
                    count += (c + 1)
                    r += 1
                else:
                    c -= 1
            return count
        lower, upper = matrix[0][0], matrix[-1][-1]
        # x is the smallest element for which the number of smaller or equal
        # elements in the matrix is k
        x = None
        while lower <= upper:
            mid = (lower + upper) // 2
            new = num_elems_leq_than(mid)
            if new >= k:
                x = min(x, mid) if x is not None else mid
                upper = mid - 1
            else:
                lower = mid + 1
        return x

sol = Solution()
assert sol.kthSmallest(
    matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
) == 13
assert sol.kthSmallest(
    matrix = [[-5]], k = 1
) == -5

assert sol.kthSmallest(
    matrix = [[1,2],[1,3]], k = 1
) == 1