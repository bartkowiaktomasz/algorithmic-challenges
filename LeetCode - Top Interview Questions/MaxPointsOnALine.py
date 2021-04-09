from typing import List
from collections import Counter, defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = defaultdict(set)  # (a, b) -> set()
        n = len(points)
        max_points = 0 if n == 0 else 1
        for i in range(n):
            for j in range(i + 1, n):
                a_nomin = points[j][1] - points[i][1]
                a_denomin = (points[j][0] - points[i][0])
                gcd = self.gcd(a_nomin, a_denomin)
                a_nomin /= gcd
                a_denomin /= gcd
                b_nomin = (points[i][1] * a_denomin - a_nomin * points[i][0])
                # b_denomin == a_denomin
                lines[(str(a_nomin), str(a_denomin), str(b_nomin))].add((points[i][0], points[i][1]))
                lines[(str(a_nomin), str(a_denomin), str(b_nomin))].add((points[j][0], points[j][1]))
                max_points = max(max_points, len(lines[(str(a_nomin), str(a_denomin), str(b_nomin))]))
        return max_points


    def gcd(self, a: int, b: int) -> int:
        """
        Euclid's algorithm for GCD
        """
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
            

sol = Solution()
points = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
print(
    sol.maxPoints(points)
)
