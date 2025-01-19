class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            print(i, j)
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if (i, j) in cache:
                return cache[(i, j)]

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j < len(p) - 1 and p[j + 1] == "*":
                cache[(i, j)] = (match and (dfs(i + 1, j) or dfs(i, j + 2))) or dfs(i, j + 2)
            else:
                cache[(i, j)] = match and dfs(i + 1, j + 1)

            return cache[(i, j)]

        return dfs(0, 0)