"""
Given the number of trailing days d and a client's total daily expenditures
for a period of n days, find and print the number of times the client will
receive a notification over all n days.
"""
import math

MAX_EXPENDITURE = 201


def build_count_arr(arr):
    count_arr = [0 for _ in range(MAX_EXPENDITURE)]
    for elem in arr:
        count_arr[elem] += 1
    return count_arr


def build_cum_count_arr(arr):
    for i in range(1, len(arr[1:])):
        arr[i] += arr[i - 1]
    return arr


def median_from_cum_count_arr(cum_count_arr, d):
    def _bsearch(arr, median_idx, i, j):
        m = (j + i) // 2
        if arr[m] == median_idx and arr[m-1] < median_idx:
            return m
        if arr[m] > median_idx and arr[m-1] < median_idx:
            return m
        elif arr[m] == median_idx and arr[m-1] == median_idx:
            return _bsearch(arr, median_idx, i=i, j=m)
        # arr[m] == median_idx and arr[m-1] > median_idx impossible cum arr
        #   must increase
        elif arr[m] < median_idx:
            return _bsearch(arr, median_idx, i=m, j=j)
        elif arr[m] > median_idx:
            return _bsearch(arr, median_idx, i=i, j=m)

    l = len(cum_count_arr)
    if d % 2 == 1:
        return _bsearch(cum_count_arr, math.ceil(d/2), i=0, j=l-1)
    else:
        return (_bsearch(cum_count_arr, d//2, i=0, j=l-1) + _bsearch(cum_count_arr, d//2 + 1, i=0, j=l-1))/2


def activityNotifications(expenditure, d):
    count_arr = build_count_arr(expenditure[:d])
    cum_count_arr = build_cum_count_arr(count_arr)
    count_notif = 0
    for exp_idx in range(d, len(expenditure)):
        median = median_from_cum_count_arr(cum_count_arr, d)
        if expenditure[exp_idx] >= 2 * median:
            count_notif += 1
        # Update cumulative count array (remove last expense and add newest)
        for i in range(expenditure[exp_idx], MAX_EXPENDITURE):
            cum_count_arr[i] += 1
        for i in range(expenditure[exp_idx-d], MAX_EXPENDITURE):
            cum_count_arr[i] -= 1
    return count_notif


# Test: expect 0
arr = list(map(int, "1 2 3 4 4".split(" ")))
print(activityNotifications(arr, 4))
