from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        i, j = 0, len(p) - 1
        letters_p = Counter(p)
        letters_s = Counter(s[i: j + 1])
        # diff = Counter({k: letters_p.get(k, 0) - letters_s.get(k, 0) for k in letters_p.keys()})
        letters_p.subtract(letters_s)
        diff = Counter({k: v for k, v in letters_p.items() if v != 0})
        res = []
        while True:
            if len(diff) == 0:
                res.append(i)
            i += 1
            j += 1
            if j == len(s):
                break
            diff[s[j]] += -1
            if diff[s[j]] == 0:
                del diff[s[j]]
            diff[s[i - 1]] += 1
            if diff[s[i - 1]] == 0:
                del diff[s[i - 1]]
        return res

sol = Solution()
s = "cbaebabacd"
p = "abc"

s2 = "abab"
p2 = "ab"

s3 = "baa"
p3 = "aa"

s4 = "aa"
p4 = "bb"
assert sol.findAnagrams(s, p) == [0, 6]
assert sol.findAnagrams(s2, p2) == [0, 1, 2]
assert sol.findAnagrams(s3, p3) == [1]
assert sol.findAnagrams(s4, p4) == []



