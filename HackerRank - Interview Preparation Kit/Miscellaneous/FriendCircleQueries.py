"""
You will be given q queries. After each query, you need to report the size of
the largest friend circle (the largest group of friends) formed after
considering that query.
"""

import os


def find(x):
    if x.parent == None:
        return x
    else:
        x.parent = find(x.parent) # path compression
        return x.parent

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root.num_children > y_root.num_children:
        y_root.parent = x_root
        x_root.num_children += 1 + y_root.num_children
        return x_root.num_children + 1
    elif x_root.num_children < y.num_children:
        x_root.parent = y_root
        y_root.num_children += 1 + x_root.num_children
        return y_root.num_children + 1
    elif x_root != y_root:
        y_root.parent = x_root
        x_root.num_children += 1 + y_root.num_children
        return x_root.num_children + 1

    return x_root.num_children

class Node():
    def __init__(self, label):
        self.label = label
        self.num_children = 0
        self.parent = None

# Complete the maxCircle function below.
def maxCircle(queries):
    label_to_node_dict = {}
    max_group = 0
    max_group_list = []
    for query in queries:
        x_label = query[0]
        y_label = query[1]
        if x_label not in label_to_node_dict:
            label_to_node_dict[x_label] = Node(x_label)
        if y_label not in label_to_node_dict:
            label_to_node_dict[y_label] = Node(y_label)
        local_max = union(label_to_node_dict[x_label], label_to_node_dict[y_label])
        max_group = max_group if max_group > local_max else local_max
        max_group_list.append(max_group)
        print(max_group)

    return max_group_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    ans = maxCircle(queries)
    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')
    fptr.close()
