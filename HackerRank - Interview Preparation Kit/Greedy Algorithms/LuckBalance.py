#!/bin/python3

# Complete the luckBalance function below.
def luckBalance(k, contests):
    sortedContests = sorted(contests, key=lambda x: x[0], reverse=True)
    luck = 0
    for contest in sortedContests:
        if contest[1] == 0:
            luck += contest[0]
        else:
            if k > 0:
                luck += contest[0]
                k += -1
            else:
                luck -= contest[0]

    return luck

