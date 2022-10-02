from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}  # letter -> last idx it appears
        partition_idxs = [-1]
        for i, c in enumerate(s): last_idx[c] = i
        partition = None
        for i, c in enumerate(s):
            if partition is None:
                partition = last_idx[c]
            if last_idx[c] > partition:
                partition = last_idx[c]
            elif i == partition:
                partition_idxs.append(partition)
                partition = None
            else:
                pass
        return [
            (partition_idxs[i + 1] - partition_idxs[i]) for i in range(len(partition_idxs) - 1)
        ]

sol = Solution()
s = "ababcbacadefegdehijhklij"
# s = "eccbbbbdec"
# s = "caedbdedda"
print(
    sol.partitionLabels(s)
)