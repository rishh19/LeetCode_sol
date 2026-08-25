class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        parts = path.split("/")

        for part in parts:

            if part == "" or part == ".":
                continue

            if part == "..":
                if len(stack) > 0:
                    stack.pop()

            else:
                stack.append(part)

        return "/" + "/".join(stack)