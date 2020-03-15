"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times.
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters
will occur the same number of times. Given a string `s`, determine if it is valid.
If so, return `YES`, otherwise return `NO`
"""

import os

# Complete the isValid function below.
def isValid(s):
    dictionary = {}
    for letter in s:
        if not letter in dictionary:
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1

    frequency_dict = {}
    for key, value in dictionary.items():
        try:
            frequency_dict[value] += 1
        except:
            frequency_dict[value] = 1

    if len(frequency_dict) == 1:
        return "YES"
    if len(frequency_dict) > 2:
        return "NO"

    first_key = int(list(frequency_dict.items())[0][0])
    second_key = int(list(frequency_dict.items())[1][0])
    first_value = int(list(frequency_dict.items())[0][1])
    second_value = int(list(frequency_dict.items())[1][1])

    if first_key == 1 and first_value == 1 or second_key == 1 and second_value == 1:
        return "YES"

    if abs(first_key - second_key) == 1:
        if first_key > second_key:
            if first_value == 1:
                return "YES"
        elif second_key > first_key:
            if second_value == 1:
                return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    fptr.write(result + '\n')
    fptr.close()
