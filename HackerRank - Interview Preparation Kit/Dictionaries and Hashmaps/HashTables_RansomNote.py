"""
Given the words in the magazine and the words in the ransom note,
print `Yes` if he can replicate his ransom note _exactly_
using whole words from the magazine; otherwise, print `No`.
"""

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()
    ransom = input().rstrip().split()

    numWordsPresent = 0
    dict = {}
    for word in magazine:
        if(word not in dict):
            dict[word] = 1
        else:
            dict[word] += 1

    for word in ransom:
        if(word not in dict):
            print('No')
            exit()
        elif(dict[word] <= 0):
            print('No')
            exit()
        else:
            dict[word] += -1

    print('Yes')
