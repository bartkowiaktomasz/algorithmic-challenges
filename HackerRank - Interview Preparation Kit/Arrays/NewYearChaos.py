"""
Find the minimum number of bribes (swaps) that took place to get the queue into its
current state. One person can bribe at most two others.

e.g. [1, 2, 3, 5, 4] means one bribe (Person 5 swapped a position with Person 4)
"""

# Complete the minimumBribes function below.
def minimumBribes(q):
    for i, elem in enumerate(q):
        if (elem - 1) - i > 2:
            return "Too chaotic"
    swaps = 0
    isSwaped = False
    for i in range(0, len(q)):
        for j in range(0, len(q) - 1):
            if(q[j] > q[j + 1]):
                q[j], q[j+1] = q[j+1], q[j]
                swaps += 1
                isSwaped = True
        if(isSwaped):
            isSwaped = False
        else:
            return swaps
    return swaps

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        print(minimumBribes(q))
