"""
There is a string, s, of lowercase English letters that is repeated infinitely many
times. Given an integer, n , find and print the number of letter a's in the first n
letters of the infinite string.

e.g. s = 'abcac' and n = 10, the first 10 characters of the infinite string
are abcacabcac. There are 4 occurences of a in the string
"""

# Complete the repeatedString function below.
def repeatedString(s, n):
    cum_count_a = [0 for _ in range(len(s))]
    cum_count_a[0] = 1 if s[0] == "a" else 0
    for i, c in enumerate(s):
        if i == 0:
            continue
        if c == 'a':
            cum_count_a[i] = cum_count_a[i - 1] + 1
        else:
            cum_count_a[i] = cum_count_a[i - 1]
    reminder = 0 if (n % len(s) == 0) else cum_count_a[n % len(s) - 1]
    return cum_count_a[-1] * (n // len(s)) + reminder
