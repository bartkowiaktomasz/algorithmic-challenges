import math
import os
import random
import re
import sys

def checkBrackets(str):
    list = []

    for char in expression:
        if char == '{' or char == '(' or char == '[':
            list.append(char)
        else:
            if len(list) == 0:
                return 'NO'
            if char == '}':
                if list[len(list) - 1] == '{':
                    list.pop()
                else:
                    return 'NO'
            if char == ')':
                if list[len(list) - 1] == '(':
                    list.pop()
                else:
                    return 'NO'
            if char == ']':
                if list[len(list) - 1] == '[':
                    list.pop()
                else:
                    return 'NO'


    if len(list) == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        expression = input()
        print(checkBrackets(expression))
