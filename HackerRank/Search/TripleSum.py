"""Sum of special triplets having elements from 3 different arrays."""
import os

# Complete the triplets function below.
def triplets(a, b, c):
    # Sort and remove duplicates
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))

    num_triplets = 0
    a_idx = 0
    c_idx = 0
    # 'le' stands for 'less or equal'
    num_a_le = 0
    num_c_le = 0
    for b_elem in b:
        while a_idx < len(a) and a[a_idx] <= b_elem:
            a_idx += 1
            num_a_le += 1
        while c_idx < len(c) and c[c_idx] <= b_elem:
            c_idx += 1
            num_c_le += 1
        num_triplets += num_a_le * num_c_le
    return num_triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    lenaLenbLenc = input().split()
    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])
    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))
    ans = triplets(arra, arrb, arrc)
    fptr.write(str(ans) + '\n')
    fptr.close()
