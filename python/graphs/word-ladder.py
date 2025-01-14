class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjacency_list = {}
        words = wordList + [beginWord]
        for word in words:
            for j in range(len(word)):
                adjacency_list[word[:j] + "*" + word[j + 1:]] = adjacency_list.get(word[:j] + "*" + word[j + 1:], [])
                adjacency_list[word[:j] + "*" + word[j + 1:]].append(word)

        q = deque()
        q.append((beginWord, 1))
        visited = set()
        while q:
            current = q.popleft()

            if current[0] in visited:
                continue

            if current[0] == endWord:
                return current[1]

            visited.add(current[0])

            for i in range(len(current[0])):
                for neighbor in adjacency_list[current[0][:i] + "*" + current[0][i + 1:]]:
                    q.append((neighbor, current[1] + 1))

        return 0





