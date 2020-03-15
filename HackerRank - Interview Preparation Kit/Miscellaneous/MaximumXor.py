"""
You are given an array `arr` of `n` elements. A list of integers, `queries` is
given as an input, find the maximum values of `queries[j] xor arr[i]` for all `i`.
"""

N_BITS = 32


class Node:
    def __init__(self):
        self.left = None
        self.right = None


def build_trie(arr):
    root = Node()
    current = root
    for num in arr:
        num = to_binary(num)
        for c in num:
            if c == '1':
                if current.right is None:
                    current.right = Node()
                current = current.right
            else:
                if current.left is None:
                    current.left = Node()
                current = current.left
        current = root
    return root


def to_binary(n):
    l = len(bin(int(n))[2:])
    padding = "0" * (N_BITS - l)
    return padding + bin(int(n))[2:]


# Complete the maxXor function below.
def maxXor(arr, queries):
    trie = build_trie(arr)
    current = trie
    out = []
    for query in queries:
        query = to_binary(query)
        num = []
        for c in query:
            if c == '0':
                if current.right is not None:
                    num.append('1')
                    current = current.right
                else:
                    num.append('0')
                    current = current.left
            else:
                if current.left is not None:
                    num.append('1')
                    current = current.left
                else:
                    num.append('0')
                    current = current.right
            if current is None:
                break
        current = trie
        val = int(''.join(num), 2)
        out.append(val)
    return out


arr = "0 1 2"
queries = """
3
7
2
"""

arr = arr.split()
queries = queries.split()
print(
    maxXor(arr, queries)
)
