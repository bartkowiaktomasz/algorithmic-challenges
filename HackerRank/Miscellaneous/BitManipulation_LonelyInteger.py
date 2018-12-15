if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    dict = {}
    sum = 0
    for i in range(0, n):
        if a[i] not in dict:
            dict[a[i]] = 1
            sum += a[i]
        elif a[i] in dict and dict[a[i]] == 0:
            dict[a[i]] = 1
            sum += a[i]
        else:
            dict[a[i]] = 0
            sum -= a[i]

    print(sum)
