from collections import defaultdict
from typing import Counter, List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len, n_words, words_cnt = len(words[0]), len(words), Counter(words)
        total_len = word_len * n_words
        idxs = []
        for i in range(len(s) - total_len  + 1):  # for each start in "s"
            cur_words_cnt = Counter()
            low, high, matches = i, i + word_len, 0  # define sliding window
            # slide s[low: high] with stepsize word_len (len(words[0]))
            while (cur_word := s[low:high]) in words:  # continue sliding as long as s[low:high] is a word
                cur_words_cnt[cur_word] += 1
                matches += 1
                if (
                    cur_words_cnt[cur_word] > words_cnt[cur_word] or  # no match
                    matches == n_words  # possible match
                ): break
                low, high = high, high + word_len
            if cur_words_cnt == words_cnt: idxs.append(i)  # compare word counts
        return idxs

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
sol = Solution()
print(
    sol.findSubstring(s, words)
)