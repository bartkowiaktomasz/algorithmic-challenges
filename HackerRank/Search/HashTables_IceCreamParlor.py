# Complete the solve function below.
def solve(arr, money):
    dict = {}
    for i in range(len(arr)):
        if(arr[i] < money):
            if (money - arr[i]) in dict:
                if(i + 1 <  dict[money - arr[i]] + 1):
                    print(i + 1, dict[money - arr[i]] + 1)
                    return
                else:
                    print(dict[money - arr[i]] + 1, i + 1)
                    return
            else:
                dict[arr[i]] = i

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        solve(arr, money)
