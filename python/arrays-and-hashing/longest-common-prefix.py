class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest, longest = min(strs), max(strs)
        for i in range(len(shortest)):
            if shortest[i] != longest[i]:
                return shortest[:i]

        return shortest
