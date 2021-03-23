from typing import List, Optional
import copy

class Solution:
    def wordBreakBottomUp(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        dp = {len(s): []}
        def solve(i: int) -> Optional[List[str]]:
            # solve(i) returns a list of all phrases that can be built from s[i:]
            #   or None if it cannot build any phrase
            # Note: solve(len(s)) will return an empty list - this is an edge
            #   case allowing to concatenate answers to subproblems
            if i not in dp:
                res = []
                for split in range(i, len(s)):
                    if s[i:split + 1] in word_set:
                        tails = solve(split + 1)
                        if tails is not None:
                            # This will be executed also if tails is an empty list where
                            #  single_res will become a list with one word
                            single_res = [s[i:split + 1] + " " + tail for tail in tails] or [s[i: split + 1]]
                            res += single_res
                dp[i] = res if res else None
            return dp[i]
        res = solve(0)
        return res if res else []

    def wordBreakRec(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        res = []
        def solve(s: str, current: List[str]):
            if not s:
                res.append(" ".join(current))
            else:
                for i in range(1, len(s) + 1):
                    if s[:i] in word_set:
                        current_cp = copy.copy(current)
                        current_cp.append(s[:i])
                        solve(s[i:], current_cp)
        solve(s, [])
        return res
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.wordBreakBottomUp(s, wordDict)

sol = Solution()
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(
    sol.wordBreak(s, wordDict)
)