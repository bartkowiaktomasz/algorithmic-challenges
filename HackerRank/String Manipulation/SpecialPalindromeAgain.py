"""
Find Special palindromic sub-strings in a string
"""
def buildListTuples(s):
    l = list()
    first = s[0]
    count = 0
    for letter in s:
        if letter == first:
            count += 1
        if letter != first:
            l.append((first, count))
            first = letter
            count = 1
    l.append((first, count))
    return l

# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    l = buildListTuples(s)
    for tup in l:
        num = tup[1]
        count += (num*(num+1))/2  # Num of substrings we can create of a string of length `num`
    if len(l) < 3:  # No way to have a middle element
        return int(count)
    else:
        for i in range(1, len(l) - 1):  # Iterate through all elements except first and last
            if l[i][1] == 1:  # One letter
                if l[i - 1][0] == l[i + 1][0]:  # Same letters around
                    l1 = l[i - 1][1]
                    l2 = l[i + 1][1]
                    count += min(l1, l2)
    return int(count)


s = "mnonopoo"
print(substrCount(len(s), s))
