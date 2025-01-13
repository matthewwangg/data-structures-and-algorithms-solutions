class TrieNode:
    def __init__(self):
        self.dictionary = {}
        self.end = False


class Trie:
    def __init__(self):
        self.node = TrieNode()

    def add(self, word) -> bool:
        current = self.node
        for c in word:
            if c not in current.dictionary:
                current.dictionary[c] = TrieNode()
            current = current.dictionary[c]

        current.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        trie = Trie()
        q = deque()
        answer = set()
        visited = set()

        for word in words:
            trie.add(word)

        def dfs(i, j, current, prefix):
            if (i, j) in visited or i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][
                j] not in current.dictionary:
                return

            visited.add((i, j))
            nextprefix = prefix + board[i][j]
            current = current.dictionary[board[i][j]]

            if current.end:
                answer.add(nextprefix)

            for neighbor in neighbors:
                dfs(i + neighbor[0], j + neighbor[1], current, nextprefix)

            visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.node, "")

        return list(answer)








