class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splits = path.split("/")
        for directory in splits:
            if not directory or directory == ".":
                continue
            if directory == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(directory)

        return "/" + "/".join(stack)
