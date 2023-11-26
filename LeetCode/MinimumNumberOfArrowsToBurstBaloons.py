from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points_sorted = sorted(points, key=lambda p: (p[1]))
        res, high = 1, points_sorted[0][1]
        for start, end in points_sorted:
            if start > high:
                res += 1
                high = end
        return res

    
s = Solution()
l1 = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]] # 2
l2 = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]] # 2
l3 = [[1,2],[3,4],[5,6],[7,8]] # 4
l4 = [[10,16],[2,8],[1,6],[7,12]] # 2
l5 = [[1,9],[7,16],[2,5],[7,12],[9,11],[2,10],[9,16],[3,9],[1,3]] # 2
l6 = [[-1,1],[0,1],[2,3],[1,2]] # 2
print(
    s.findMinArrowShots(
        l3
    )
)