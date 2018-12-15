"""
How many deletions needed to make two strings anagrams?
"""


def numSameLetters(str1, str2):
    dict = {}
    numSame = 0
    for char in str1:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    for char in str2:
        if char in dict and dict[char] > 0:
            numSame += 1
            dict[char] += -1

    return numSame


if __name__ == '__main__':
    dict = {}
    a = input()
    b = input()
    num = numSameLetters(a, b)
    print(len(a) - num + len(b) - num)
