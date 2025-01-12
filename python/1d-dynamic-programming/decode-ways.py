class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dfs(index):
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            if index in cache:
                return cache[index]

            cache[index] = dfs(index + 1)
            if index < len(s) - 1 and (s[index] == "1" or (s[index] == "2" and int(s[index + 1]) < 7)):
                cache[index] += dfs(index + 2)

            return cache[index]

        return dfs(0)
