"""
You are given pointer to the root of the Huffman tree and a binary coded string
to decode. You need to print the decoded string.
"""

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    word = list()
    node = root
    i = 0
    while i < len(s):
        bit = s[i]
        if node.data.isalpha():
            word.append(node.data)
            node = root
        else:
            if bit == '0':
                node = node.left
            elif bit == '1':
                node = node.right
            i += 1
    word.append(node.data)
    print(''.join(word))
