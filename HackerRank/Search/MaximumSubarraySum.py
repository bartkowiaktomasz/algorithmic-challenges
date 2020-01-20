"""
Complete the maximumSum function in the editor below. It should return a long
integer that represents the maximum value of a sum(subarray) mod m.

NOTE:
    subarray is contiguous, subsequence is not!
"""
import bisect


# Complete the maximumSum function below.
def maximumSum(a, m):
    prefix_sum = [a[0] % m]
    prefix_sum_sorted = [a[0] % m]
    current_max = prefix_sum_sorted[0]
    for elem in a[1:]:
        prefix_sum_next = (prefix_sum[-1] + elem) % m
        prefix_sum.append(prefix_sum_next)
        idx_closest_bigger = bisect.bisect_right(prefix_sum_sorted, prefix_sum_next)
        if idx_closest_bigger >= len(prefix_sum_sorted):
            current_max = max(current_max, prefix_sum_next)
            bisect.insort_right(prefix_sum_sorted, prefix_sum_next)
            continue
        if prefix_sum_sorted[idx_closest_bigger] > prefix_sum_next:
            current_max = max(current_max, (prefix_sum_next - prefix_sum_sorted[idx_closest_bigger]) % m)
            bisect.insort_right(prefix_sum_sorted, prefix_sum_next)
    return current_max


arr = [3, 3, 9, 9, 5]
m = 7
maximumSum(arr, m)
