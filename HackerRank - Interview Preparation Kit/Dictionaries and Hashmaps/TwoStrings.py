"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.
For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.
"""

import os

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    minLength = len(s1) if len(s1) <= len(s2) else len(s2)
    hashmap_s1 = {}
    hashmap_s2 = {}
    print(minLength)
    for i in range(minLength):
        letter_s1 = s1[i]
        letter_s2 = s2[i]
        if not letter_s1 in hashmap_s1:
            hashmap_s1[letter_s1] = 1
        if letter_s2 in hashmap_s1:
            return "YES"
        if not letter_s2 in hashmap_s2:
            hashmap_s2[letter_s2] = 1
        if letter_s1 in hashmap_s2:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        fptr.write(result + '\n')
    fptr.close()
