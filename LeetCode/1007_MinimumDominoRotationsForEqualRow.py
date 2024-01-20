from collections import Counter
import math
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        counter_tops, counter_bottoms = Counter(tops), Counter(bottoms)
        counter_equal = Counter()
        for i in range(len(tops)): counter_equal[tops[i]] += int(tops[i] == bottoms[i])
        min_ = math.inf
        for i in range(1, 7):
            union = counter_tops[i] + counter_bottoms[i] - counter_equal[i]
            if union >= len(tops):
                min_ = min(
                    min_, len(tops) - counter_tops[i], len(tops) - counter_bottoms[i]
                )
        return min_ if min_ != math.inf else -1

        