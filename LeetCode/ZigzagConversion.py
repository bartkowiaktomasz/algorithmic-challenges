class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        The string "PAYPALISHIRING" is written in a zigzag pattern
        on a given number of rows like this: (you may want to display
        this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R

        And then read line by line: "PAHNAPLSIIGYIR"
        Write the code that will take a string and make this
        conversion given a number of rows:
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        cnt, direction, rows_idx = 0, 1, -1
        for c in s:
            if cnt == numRows: direction *= -1; cnt = 1
            rows_idx += direction
            cnt += 1
            if len(rows) < numRows:
                rows.append(c)
                continue
            rows[rows_idx] += c
        return ''.join(rows)
    
sol = Solution()
assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert sol.convert("A", 1) == "A"
assert sol.convert("ABC", 1) == "ABC"
