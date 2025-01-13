class TrieNode:
    def __init__(self):
        self.dictionary = {}
        self.ending = False


class Trie:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        current = self.node
        for c in word:
            if c not in current.dictionary:
                current.dictionary[c] = TrieNode()
            current = current.dictionary[c]

        current.ending = True

    def search(self, word: str) -> bool:
        current = self.node
        for c in word:
            if c not in current.dictionary:
                return False
            current = current.dictionary[c]

        return current.ending

    def startsWith(self, prefix: str) -> bool:
        current = self.node
        for c in prefix:
            if c not in current.dictionary:
                return False
            current = current.dictionary[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)