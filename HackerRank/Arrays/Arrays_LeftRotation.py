"""
A _left rotation_ operation on an array shifts each of the array's elements
unit to the left.
"""

def array_left_rotation(a, n, k):
    rightShift = n - k
    b = a[:]
    for i in range(0,n):
        b[(i + rightShift) % n] = a[i]
    return b

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(answer)
