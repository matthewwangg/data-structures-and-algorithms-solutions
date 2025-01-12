class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dfs(i):
            if i > len(s):
                return False
            if i == len(s):
                return True
            if i in cache:
                return cache[i]

            cache[i] = False
            for word in wordDict:
                if i + len(word) > len(s) or s[i:i + len(word)] != word:
                    continue
                cache[i] = cache[i] or dfs(i + len(word))

            return cache[i]

        return dfs(0)

