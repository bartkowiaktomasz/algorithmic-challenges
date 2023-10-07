from typing import List, Tuple


class Solution:
    def totalNQueens(self, n: int) -> int:
        def next(x: int, y: int):
            return (x + 1 if y == n - 1 else x), (0 if y == n - 1 else y + 1)
        
        if n == 1: return 1
        total = 0
        qs, (xs, ys) = [(0, 0)], (1, 0)  # Initialise the first queen at (0, 0)
        rows_occupied, cols_occupied, diag_pos_occoupied, diag_neg_occupied = set([0]), set([0]), set([0]), set([0])
        # While there are queens on the board or, if no queens, we're still considering a slot for a queen
        #   when qs is empty and xs == n then we've exhausted all options
        while qs or xs != n:
            while xs != n:
                if (
                    xs in rows_occupied or
                    ys in cols_occupied or
                    xs + ys in diag_pos_occoupied or
                    xs - ys in diag_neg_occupied
                ):
                    xs, ys = next(xs, ys)
                    continue
                else:
                    qs.append((xs, ys))
                    rows_occupied.add(xs); cols_occupied.add(ys); diag_pos_occoupied.add(xs + ys); diag_neg_occupied.add(xs - ys)
                    if len(qs) == n: total += 1
                    break
            if qs[-1] != (xs, ys):
                xs, ys = qs.pop()
                rows_occupied.remove(xs); cols_occupied.remove(ys); diag_pos_occoupied.remove(xs + ys); diag_neg_occupied.remove(xs - ys)
            xs, ys = next(xs, ys)
        return total

sol = Solution()
print(
    sol.totalNQueens(7)
)
        