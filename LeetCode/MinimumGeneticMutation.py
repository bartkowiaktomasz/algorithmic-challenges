import copy
import math
from typing import List

from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if not endGene in bank_set: return -1
        def bfs(gene: str):
            nonlocal bank_set
            visited = set()
            queue = deque([(gene, 0)])
            while queue:
                gene_str, n_mut = queue.pop()
                gene = [g for g in gene_str]
                for i in range(len(gene)):
                    temp = gene[i]
                    for g in ["A", "C", "G", "T"]:
                        if g == gene[i]: continue
                        new_gene = gene; new_gene[i] = g
                        new_gene_str = "".join(new_gene)
                        if new_gene_str == endGene: return n_mut + 1
                        if new_gene_str in bank_set and new_gene_str not in visited:
                            visited.add(new_gene_str)
                            queue.appendleft((new_gene_str, n_mut + 1))
                    gene[i] = temp
            return -1
        return bfs(startGene)


s = "AACCGGTT"; e = "AACCGCTA"; b = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2:    AACCGGTT -> AACCGGTA -> AACCGCTA
s = "AACCGGTT"; e = "AACCGGTA"; b = ["AACCGGTA"]
# Output: 1
s = "AACCGGTT"; e = "AAACGGTA"; b = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
sol = Solution()
print(
    sol.minMutation(s, e, b)
)