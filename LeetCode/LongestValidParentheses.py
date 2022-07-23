class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                if stack:
                    l = i - stack[-1]
                    max_length = max(max_length, l)
                else:
                    stack.append(i)
        return max_length


sol = Solution()
assert sol.longestValidParentheses("()") == 2
assert sol.longestValidParentheses("(()") == 2
assert sol.longestValidParentheses("(") == 0
assert sol.longestValidParentheses("()") == 2
assert sol.longestValidParentheses("()(())") == 6
assert sol.longestValidParentheses("()(()") == 2
assert sol.longestValidParentheses("(()(((()") == 2
assert sol.longestValidParentheses("(()()") == 4