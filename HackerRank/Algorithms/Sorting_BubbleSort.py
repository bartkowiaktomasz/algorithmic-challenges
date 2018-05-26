def swap(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

    return list

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


noSwaps = 0
for i in range(n, 0, -1):
    for j in range(0, i - 1):
        if(a[j + 1] < a[j]):
            a = swap(a, j, j + 1)
            noSwaps += 1

print("Array is sorted in", noSwaps, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[n - 1])
