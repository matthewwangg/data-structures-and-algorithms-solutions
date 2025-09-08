class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        cache = {}
        def construct(i):
            if i == len(s):
                return 0

            if i in cache:
                return cache[i]
            
            cache[i] = construct(i+1) + 1
            for word in dictionary:
                if i + len(word) > len(s) or s[i:i+len(word)] != word:
                    continue
                cache[i] = min(cache[i], construct(i+len(word)))
                        
            return cache[i]
        
        return construct(0)
