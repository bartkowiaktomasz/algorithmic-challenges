"""
Process the insert/delete queries and report if any integer is there with a
particular frequency
"""
from collections import defaultdict


def freqQuery(queries):
    freq_to_ints = defaultdict(set)
    num_to_freq = defaultdict(int)
    ret = list()
    for query in queries:
        op = query[0]
        num = query[1]
        if op == 1:
            if num in freq_to_ints[num_to_freq[num]]:
                    freq_to_ints[num_to_freq[num]].remove(num)
            num_to_freq[num] += 1
            freq_to_ints[num_to_freq[num]].add(num)
        if op == 2:
            if num_to_freq[num] > 0:
                if num in freq_to_ints[num_to_freq[num]]:
                    freq_to_ints[num_to_freq[num]].remove(num)
                num_to_freq[num] -= 1
                freq_to_ints[num_to_freq[num]].add(num)
        if op == 3:
            ret.append(1 if len(freq_to_ints[num]) > 0 else 0)
    return ret

l = \
[tuple(map(int, elem.split(" "))) for elem in
"""1 3
2 3
3 2
1 4
1 5
1 5
1 4
3 2
2 4
3 2"""
.split("\n")]
print(freqQuery(l))
