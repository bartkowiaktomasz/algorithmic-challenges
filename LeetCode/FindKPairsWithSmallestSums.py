from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Optimisation
        if k == 1: return [nums1[0], nums2[0]]
        min_heap, result, heap_elems = [], [], set([(0, 0)])
        heapq.heappush(min_heap, (nums1[0] + nums2[0], (0, 0)))
        
        while len(result) < k and min_heap:
            _, idxs = heapq.heappop(min_heap)
            i, j = idxs[0], idxs[1]
            result.append([nums1[i], nums2[j]])
            heap_elems.remove((i, j))
            if (i + 1, j) not in heap_elems and i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                heap_elems.add((i + 1, j))
            if (i, j + 1) not in heap_elems and j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                heap_elems.add((i, j + 1))
        return result

    

sol = Solution()
nums1 = [1,7,11]; nums2 = [2,4,6]; k = 3
nums1 = [1,1,2]; nums2 = [1,2,3]; k = 2
nums1 = [1,2]; nums2 = [3]; k = 3
nums1 = [1]; nums2 = [3,5,6,7,8,100]; k = 4
nums1 = [-10,-4,0,0,6]; nums2 = [3,5,6,7,8,100]; k = 10
print(
    sol.kSmallestPairs(nums1, nums2, k)
)