class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        finalanswer = []

        startingboard = ["." * n for _ in range(n)]

        def valid(board, pos):
            for i in range(n):
                if board[i][pos[1]] == "Q":
                    return False
                if board[pos[0]][i] == "Q":
                    return False
                if i + pos[0] < n and i + pos[1] < n and board[pos[0] + i][pos[1] + i] == "Q":
                    return False
                if i + pos[0] < n and pos[1] - i > -1 and board[pos[0] + i][pos[1] - i] == "Q":
                    return False
                if pos[0] - i > -1 and i + pos[1] < n and board[pos[0] - i][pos[1] + i] == "Q":
                    return False
                if pos[0] - i > -1 and pos[1] - i > -1 and board[pos[0] - i][pos[1] - i] == "Q":
                    return False

            return True

        def buildrow(index):
            row = ""
            for i in range(n):
                if i != index:
                    row += "."
                else:
                    row += "Q"

            return row

        def backtracker(count, board):
            if count == n:
                finalanswer.append(board[:])
                return

            for i in range(n):
                if valid(board, (count, i)):
                    board[count] = buildrow(i)
                    backtracker(count + 1, board)
                    board[count] = buildrow(-1)

        backtracker(0, startingboard)
        return finalanswer