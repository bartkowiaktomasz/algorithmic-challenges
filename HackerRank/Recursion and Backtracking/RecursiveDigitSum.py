import os

def superDigit_rec(n):
    if len(str(n)) == 1:
        return n
    else:
        s = sum([int(d) for d in str(n)])
        return superDigit_rec(s)

# Complete the superDigit function below.
def superDigit(n, k):
    s = sum([int(d) for d in str(n)])
    return superDigit_rec(k*s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
