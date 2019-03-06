"""
You are planning production for an order. You have a number of machines that
each have a fixed number of days to produce an item. Given that all the
machines operate simultaneously, determine the minimum number of days to
produce the required order.
"""

import math
import os

_machines = None
GOAL = None

def num_items(days):
    s = sum([math.floor(float(days)/m) for m in _machines])
    return int(s)

# Complete the min_time function below.
def min_time(machines, goal):
    global GOAL, _machines
    _machines = sorted(machines)
    GOAL = goal
    low_bound = 1
    # Worst case for a machine when it needs 1e9 days and the goal is 1e9
    up_bound = int(1e18)
    day = up_bound // 2
    while low_bound < up_bound:
        if num_items(day) >= GOAL and num_items(day - 1) < GOAL:
            return day
        if low_bound == day:
            return up_bound
        elif num_items(day) >= GOAL:
            up_bound = day
            day = (low_bound + up_bound) // 2
        elif num_items(day) < GOAL:
            low_bound = day
            day = (low_bound + up_bound) // 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nGoal = input().split()
    n = int(nGoal[0])
    goal = int(nGoal[1])
    machines = list(map(int, input().rstrip().split()))
    ans = min_time(machines, goal)
    fptr.write(str(ans) + '\n')
    fptr.close()
