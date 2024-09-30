class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def backtracker(pos, index, visited):
            visited.add(pos)

            for i in neighbors:
                if pos[0] + i[0] < 0 or pos[0] + i[0] == len(board) or pos[1] + i[1] < 0 or pos[1] + i[1] == len(
                        board[0]) or (pos[0] + i[0], pos[1] + i[1]) in visited:
                    continue

                if index == len(word) - 1 and board[pos[0] + i[0]][pos[1] + i[1]] == word[index]:
                    return True

                if board[pos[0] + i[0]][pos[1] + i[1]] == word[index]:
                    if backtracker((pos[0] + i[0], pos[1] + i[1]), index + 1, visited):
                        return True
            visited.remove(pos)
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if len(word) == 1 or backtracker((i, j), 1, set()):
                        return True

        return False
