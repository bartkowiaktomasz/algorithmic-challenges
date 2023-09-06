class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == ".":
                continue
            elif p == "..":
                if stack: stack.pop()
            elif p:
                stack.append(p)
        return "/" + "/".join(stack)

sol = Solution()
print(
    sol.simplifyPath("/...")
)