"""
There is a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus. The player can jump on
any cumulus cloud having a number that is equal to the number of the current cloud
plus 1 or 2. The player must avoid the thunderheads.

Determine the minimum number of jumps it will take to jump from the starting postion to
the last cloud. It is always possible to win the game.
"""
import sys


def jumpingOnCloudsRecursive(c, current, num_jumps):
    if current == (len(c) - 1):
        return num_jumps
    # We are not on the finish line
    if current + 2 == len(c):
        current += 1
        return jumpingOnCloudsRecursive(c, current, num_jumps + 1)
    if (c[current + 1] == 0) and (c[current + 2] == 1):
        current += 1
        return jumpingOnCloudsRecursive(c, current, num_jumps + 1)
    elif (c[current + 1] == 1) and (c[current + 2] == 0):
        current += 2
        return jumpingOnCloudsRecursive(c, current, num_jumps + 1)
    elif (c[current + 1] == 1) and (c[current + 2] == 1):
        # Both to avoid
        return sys.maxsize
    else:
        return min(
            jumpingOnCloudsRecursive(c, current + 1, num_jumps + 1),
            jumpingOnCloudsRecursive(c, current + 2, num_jumps + 1)
    )


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current = 0
    num_jumps = 0
    return jumpingOnCloudsRecursive(c, current, num_jumps)
