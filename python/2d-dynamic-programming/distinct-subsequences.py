class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def match(i, j):
            if len(t) == j:
                return 1
            if len(s) == i:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            cache[(i, j)] = match(i + 1, j)

            if s[i] == t[j]:
                cache[(i, j)] += match(i + 1, j + 1)

            return cache[(i, j)]

        return match(0, 0)


