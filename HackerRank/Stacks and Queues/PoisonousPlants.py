"""
There are a number of plants in a garden. Each of these plants has been
treated with some amount of pesticide. After each day, if any plant has more
pesticide than the plant on its left, being weaker than the left one, it dies.

You are given the initial values of the pesticide in each of the plants. Print
the number of days after which no plant dies, i.e. the time after which there
are no plants with more pesticide content than the plant to their left.

For example, pesticide levels p=[3,6,2,7,5]. Using a 1-indexed array,
day 1 plants 2 and 4 die leaving p=[3,2,5]. On day 2, plant 3 of the current
array dies leaving p=[3,2]. As there is no plant with a higher concentration of
pesticide than the one to its left, plants stop dying after day 2.
"""

def build_non_increasing_stacks(p):
    """Partition `p` into list of non-increasing stacks"""
    stacks = []
    cur_stack = [p[0]]
    for elem in p[1:]:
        if elem <= cur_stack[-1]:
            cur_stack.append(elem)
        else:
            stacks.append(cur_stack)
            cur_stack = [elem]
    if cur_stack:
        stacks.append(cur_stack)
    return stacks


def merge(stacks):
    """Given a list of stacks, merge neighbouring stacks
    if they can form a bigger stack with non-increasing elements"""
    merged_stacks = [stacks[0]]
    previous_stack = stacks[0]
    for stack in stacks[1:]:
        if previous_stack[-1] >= stack[0]:
            merged_stacks[-1] = previous_stack + stack
        else:
            merged_stacks.append(stack)
        previous_stack = merged_stacks[-1]
    return merged_stacks


def poisonousPlants(p):
    stacks = build_non_increasing_stacks(p)
    days = 0
    while not len(stacks) == 1:
        stacks[1:] = [s for s in stacks[1:] if len(s) != 1]
        for stack in stacks[1:]:
            stack.pop(0)
        days += 1
        stacks = merge(stacks)
    return days


input1 = "6 5 8 4 7 10 9"
input2 = "4 3 7 5 6 4 2"
input3 = "3 2 5 4"
args = [int(n) for n in input1.split(" ")]
print(
    poisonousPlants(args)
)
