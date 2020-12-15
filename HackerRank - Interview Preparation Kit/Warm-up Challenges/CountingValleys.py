"""
Given the sequence of up and down steps during a hike, find and print the number of
valleys walked through.

e.g. `steps = [DDUUUUDD] means one valley of depth 2 (entered at the beginning)
"""

def countingValleys(steps, path):
    # Write your code here
    running_sum = 0
    num_valleys = 0
    for step in path:
        previous_running_sum = running_sum
        running_sum += 1 if step == "U" else -1
        if previous_running_sum == 0 and running_sum == -1:
            num_valleys += 1
    return num_valleys
