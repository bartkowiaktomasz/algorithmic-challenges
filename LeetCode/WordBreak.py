from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wordBreakBottomUp(s, wordDict)

    def wordBreakTopDown(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        n = len(s)
        dp = {}
        def solve(s):
            if not s:
                return True
            if s in dp:
                return dp[s]
            else:
                dp[s] = any([solve(s[i + 1:]) for i in range(len(s)) if s[:i + 1] in wordDictSet])
                return dp[s]
        return solve(s)

    def wordBreakBottomUp(self, s: str, wordDict: List[str]) -> bool:
        """
        can_build[i] denotes whether we can build a string s[:i]
        We can build s[:i] if there exists some j between 0 and i for which 
        can_build[j] == True and s[j:i] is in the dictionary
        """
        word_set = set(wordDict)
        can_build = [None for _ in range(len(s) + 1)]
        can_build[0] = True
        for i in range(1, len(s) + 1):
            can_build[i] = any([can_build[j] and s[j:i] in word_set for j in range(i)])
        print(can_build)
        return can_build[-1]
        
        
sol = Solution()
s = "leetcode"
wordDict = ["leet","code"]
print(
    sol.wordBreak(s, wordDict)
)