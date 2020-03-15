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
