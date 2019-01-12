"""
Alice is a kindergarten teacher. She wants to give some candies to the children in her class. All the children sit
in a line and each of them has a rating score according to his or her performance in the class. Alice wants
to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating
must get more candies. Alice wants to minimize the total number of candies she must buy.
"""

import os


def list_pass(arr):
    print(arr)
    n = len(arr)
    count_list = [None for _ in range(n)]
    count_list[0] = 1
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            count_list[i] = count_list[i - 1] + 1
        else:
            count_list[i] = 1

    return count_list


# Complete the candies function below.
def candies(n, arr):
    arr_reversed = arr[::-1]
    left_right_count = list_pass(arr)
    right_left_count = list_pass(arr_reversed)[::-1]

    print(left_right_count, right_left_count)
    count = [max(left_right_count[i], right_left_count[i]) for i in range(n)]
    return sum(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
