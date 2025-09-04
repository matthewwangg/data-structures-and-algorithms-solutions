class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sentences = []
        def dfs(i, sentence):
            if i == len(s):
                sentences.append(" ".join(sentence))
                return

            for word in wordDict:
                if i + len(word) > len(s) or s[i:i + len(word)] != word:
                    continue
                sentence.append(word)
                dfs(i + len(word), sentence)
                sentence.pop()

        dfs(0, [])

        return sentences
