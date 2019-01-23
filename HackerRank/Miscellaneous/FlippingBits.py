"""
You will be given a list of 32 bit unsigned integers. Flip all the bits and
print the result as an unsigned integer.
"""
import os


# Complete the flippingBits function below.
def flippingBits(n):
    string = bin(n)[2:]
    padding_len = 32 - len(string)
    return int('0'*padding_len + string, 2) ^ int('1'*32, 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        result = flippingBits(n)
        fptr.write(str(result) + '\n')
    fptr.close()
