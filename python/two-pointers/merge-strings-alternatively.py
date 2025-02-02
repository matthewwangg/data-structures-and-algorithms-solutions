class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        mergedString = ""

        for i in range(n):
            mergedString += word1[i] + word2[i]

        mergedString += word1[n:] + word2[n:]
        return mergedString
