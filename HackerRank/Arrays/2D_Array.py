"""
A left rotation operation on an array shifts each of the array's elements  unit to the left.
"""
import os

# Given coordinates of a glass center, compute its sum
def singleGlassSum(arr, x_center, y_center):
    upper = arr[x_center - 1][y_center - 1] + arr[x_center - 1][y_center] + arr[x_center - 1][y_center + 1]
    lower = arr[x_center + 1][y_center - 1] + arr[x_center + 1][y_center] + arr[x_center + 1][y_center + 1]
    return upper + arr[x_center][y_center] + lower

# Complete the hourglassSum function below.
def hourglassSum(arr):
    for x in range(1, 5):
        for y in range(1, 5):
            if x == 1 and y == 1:
                maxSum = singleGlassSum(arr, x, y)
            sum = singleGlassSum(arr, x, y)
            if(sum > maxSum):
                maxSum = sum

    return maxSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
