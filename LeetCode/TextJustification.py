from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur_words, cur_len = [], [], 0
        for w in words:
            if cur_len + (len(cur_words)) + len(w) > maxWidth:
                line = []
                if len(cur_words) > 1:
                    spacing = (maxWidth - cur_len) // (len(cur_words) - 1)
                    n_spaces_left = (maxWidth - cur_len) % (len(cur_words) - 1)
                for cw in cur_words[:-1]:
                    cur_line = cw + spacing * " "
                    if n_spaces_left > 0:
                        cur_line += " "
                        n_spaces_left -= 1
                    line.append(cur_line)
                line.append(cur_words[-1])
                line = "".join(line).ljust(maxWidth)
                res.append(line)
                cur_len, cur_words = len(w), [w]
            else:
                cur_len += len(w)
                cur_words += [w]
        if cur_words:
            res.append(" ".join(cur_words).ljust(maxWidth))
        return res

sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 16
print(
    sol.fullJustify(
        words, 20
    )
)