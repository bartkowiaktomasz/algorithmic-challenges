from typing import List, Set, Tuple
from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        def dfs(i: int, j: int, word: str, visited: Set[Tuple[int]]) -> bool:
            if not word:
                return True
            if not (0 <= i < n):
                return False
            if not (0 <= j < m):
                return False
            if (i, j) in visited:
                return False
            if board[i][j] != word[0]:
                return False
            visited.add((i, j))
            res = (
                dfs(i + 1, j, word[1:], visited)
                or dfs(i, j + 1, word[1:], visited) 
                or dfs(i - 1, j, word[1:], visited)
                or dfs(i, j - 1, word[1:], visited)
            )
            visited.remove((i, j))
            return res
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i, j, word, visited):
                        return True
        return False


                
s = Solution()
board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
print(
    s.exist([["a"]], "a")
)