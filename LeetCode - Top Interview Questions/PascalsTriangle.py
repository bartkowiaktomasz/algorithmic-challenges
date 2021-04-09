from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        current_row = [1]
        res = [current_row]
        for i in range(2, numRows + 1):
            row = []
            i = 0
            j = 1
            row.append(1)
            while j < len(res[-1]):
                row.append(res[-1][i] + res[-1][j])
                i += 1
                j += 1
            row.append(1)
            res.append(row)
        return res
