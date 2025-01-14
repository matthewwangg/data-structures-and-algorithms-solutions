class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        starts = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    starts.append([i, j])

        def dfs(pos):
            if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(board) or pos[1] >= len(board[0]) or board[pos[0]][
                pos[1]] != "O":
                return

            board[pos[0]][pos[1]] = "."

            for n in neighbors:
                dfs([pos[0] + n[0], pos[1] + n[1]])

        for pos in starts:
            dfs(pos)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == ".":
                    board[i][j] = "O"