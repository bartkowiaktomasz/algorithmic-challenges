"""Fill in the crossword of size 10x10 with given list of words"""
import os
from collections import deque

# Globals
HOR = 0
VER = 1

def length(c, i, j, direction):
    count = 0
    if direction == HOR:
        while j < 10 and c[i][j] == '-':
            count += 1
            j += 1
    elif direction == VER:
        while i < 10 and c[i][j] == '-':
            count += 1
            i += 1
    return count

def horizonal_start(c, i, j):
    if c[i][j] != '-':
        return False
    elif j == 9:
        return False
    elif c[i][j+1] == '-':
        if j == 0:
            return True
        elif j != 0 and c[i][j-1] != '-':
            return True
    return False

def vertical_start(c, i, j):
    if c[i][j] != '-':
        return False
    elif i == 9:
        return False
    elif c[i+1][j] == '-':
        if i == 0:
            return True
        elif i != 0 and c[i-1][j] != '-':
            return True
    return False

def insert(word, position, crossword):
    i, j, direction, length = position
    for letter in word:
        if crossword[i][j] != '+' and crossword[i][j] != 'X' and not \
                (crossword[i][j].isalpha() and crossword[i][j] != letter):
            crossword[i][j] = letter
        else:
            return False
        if direction == HOR:
            j += 1
        else:
            i += 1
    print("Inserting " + word + " at " + str(i) + "," + str(j))
    return crossword

def can_remove_letter(crossword, i, j, direction):
    if crossword[i][j] == 'X' or crossword[i][j] == '+':
        return False
    if direction == HOR:
        if 1 < i < 9:
            if not crossword[i+1][j].isalpha() and not crossword[i-1][j].isalpha():
                return True
            else:
                return False
        if i == 9:
            if not crossword[i-1][j].isalpha():
                return True
            else:
                return False
        if i == 1:
            if not crossword[i+1][j].isalpha():
                return True
            else:
                return False
    if direction == VER:
        if 1 < j < 9:
            if not crossword[i][j+1].isalpha() and not crossword[i][j+1].isalpha():
                return True
            else:
                return False
        if j == 9:
            if not crossword[i][j-1].isalpha():
                return True
            else:
                return False
        if j == 1:
            if not crossword[i][j+1].isalpha():
                return True
            else:
                return False

def revert(crossword, position):
    i, j, direction, length = position
    while crossword[i][j] != '+' or crossword[i][j] != 'X':
        if can_remove_letter(crossword, i, j, direction):
            crossword[i][j] = '-'
        if direction == HOR:
            j += 1
        else:
            i += 1
        if i == 10 or j == 10:
            return crossword
    return crossword

def solve(crossword, words, positions_stack):
    if len(positions_stack) == 0:
        return True

    position = positions_stack.pop()
    i, j, direction, length = position
    for word in words:
        if len(word) != length:
            continue
        if insert(word, position, crossword) and \
        solve(crossword, words, positions_stack):
                return True
        revert(crossword, position)
    revert(crossword, position)
    positions_stack.appendleft(position)
    return False

def build_positions_stack(crossword):
    positions_stack = deque()
    for i in range(10):
        for j in range(10):
            if horizonal_start(crossword, i, j):
                l = length(crossword, i, j, HOR)
                positions_stack.append((i, j, HOR, l))
            elif vertical_start(crossword, i , j):
                l = length(crossword, i, j, VER)
                positions_stack.append((i, j, VER, l))
    return positions_stack

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    crossword_matrix = [list(row) for row in crossword]
    positions_stack = build_positions_stack(crossword_matrix)
    words = deque(words.split(';'))
    solve(crossword_matrix, words, positions_stack)
    out = []
    for row in crossword_matrix:
        out.append(''.join(row))
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    crossword = []
    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)
    words = input()
    result = crosswordPuzzle(crossword, words)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
