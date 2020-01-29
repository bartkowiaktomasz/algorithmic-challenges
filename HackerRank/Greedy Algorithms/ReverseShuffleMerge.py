"""
Given a string S such that s = merge(reverse(A), shuffle(A))
for some string A, find the lexicographically smallest A.
- "shuffle" is any permutation of the string
- "merge(a, b)" is an interspersing of "a" and "b" that maintains the order
of the characters
"""
from collections import defaultdict


def build_counter(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d


def can_pop(char, to_be_seen_count, left_to_be_used_count):
    return ((to_be_seen_count[char] > left_to_be_used_count[char])
            and (to_be_seen_count[char] >= left_to_be_used_count[char]))


def reverseShuffleMerge(s):
    s = s[::-1]
    left_to_be_used_count = build_counter(s)
    for char, count in left_to_be_used_count.items():
        left_to_be_used_count[char] = count // 2
    to_be_seen_count = build_counter(s)

    output = []
    for char in s:
        to_be_seen_count[char] -= 1
        if left_to_be_used_count[char] > 0:
            while output and (output[-1] > char) and can_pop(output[-1], to_be_seen_count, left_to_be_used_count):
                elem = output.pop()
                left_to_be_used_count[elem] += 1
            output.append(char)
            left_to_be_used_count[char] -= 1
    return ''.join(output)


st = 'aahaxxxhxhxxah'  # Expected: ahhxxxa
st2 = 'aabbccbb'  # Expected: bbca
st3 = 'aeiouuoiea'  # Expected: aeiou
st4 = 'abeeba'  # Expected: abe
st5 = 'aaabeeba'  # Expected: abea
st6 = 'aacdbdcb'  # Expected: bcda
st7 = 'aaccddbddccb'  # Expected: bccdda
st8 = 'eggegg'  # Expected: egg

print(reverseShuffleMerge(st))
