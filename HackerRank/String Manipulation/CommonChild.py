"""
A string is said to be a child of a another string if it can be formed by
deleting 0 or more characters from the other string. Given two strings of equal
length, what's the longest string that can be constructed such that it is a
child of both?
"""

def commonChild(s1, s2):
    arr = [[0]*(len(s1) + 1) for _ in range(len(s2) + 1)]
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s1[j] == s2[i]:
                arr[i + 1][j + 1] = arr[i][j] + 1
            else:
                arr[i + 1][j + 1] = max(arr[i + 1][j], arr[i][j + 1])
    return arr[-1][-1]

# Test
# Expected: 3 ("NHA")
s1 = "SHINCHAN"
s2 = "NOHARAAA"
print(commonChild(s1, s2))
