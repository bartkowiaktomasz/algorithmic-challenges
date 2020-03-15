"""
You are given a string containing characters A and B only. Your task is to change it
into a string such that there are no matching adjacent characters. To do this, you
are allowed to delete zero or more characters in the string.
"""


import os


def areAjacentSame(s):
    if s[0] == s[1]:
        return True
    else:
        return False


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = 0
    j = 0
    for i in range(len(s) - 1):
        if s[i+1] == s[j]:
            deletions += 1
            i += 1
        else:
            i += 1
            j = i

    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()