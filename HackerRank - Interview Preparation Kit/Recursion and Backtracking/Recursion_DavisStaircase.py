"""
Complete the stepPerms function in the editor below. It should recursively calculate
and return the integer number of ways
Davis can climb the staircase, modulo 10000000007.
"""


# Complete the stepPerms function below.
def stepPerms(n):
    # We only need last three entries, start with index 1 for simplicity
    #  i.e. memo[1] means step 1
    memo = [0 for _ in range(4)]
    memo[1] = 1
    memo[2] = 2
    # 4 ways to jump to step 3:
    #   3, 2 -> 1, 1 -> 2, 1 -> 1 -> 1
    memo[3] = 4
    if n <= 3:
        return memo[n]
    i = 4
    while i <= n:
        # inserts num -> idx:
        #  1 -> 1, 2 -> 2, 3-> 3, 4 -> 1, 5 -> 2,...
        #  such that 0th index isn't used
        memo[(i - 1) % 3 + 1] = memo[1] + memo[2] + memo[3]
        i += 1
    # i was incremented before leaving while loop so we need to access previous
    #  memoized number
    num_ways = memo[(i - 2) % 3 + 1]
    return num_ways % (pow(10, 10) + 7)


print(
    [stepPerms(n) for n in range(19)]
)

