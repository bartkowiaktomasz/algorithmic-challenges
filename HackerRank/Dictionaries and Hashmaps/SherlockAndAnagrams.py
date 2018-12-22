"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
"""

import os


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    dictionary = {}
    for length in range(1, len(s) + 1):
        for i in range(0, len(s) - length + 1):
            sorted_str = ''.join(sorted(s[i:i+length]))
            try:
                dictionary[sorted_str] += 1
            except:
                dictionary[sorted_str] = 1
    count = 0
    for key, value in dictionary.items():
        print(key, value)
        count += value * (value - 1) // 2

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + '\n')
    fptr.close()
