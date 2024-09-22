class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        neighbors = [(0, 0), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
        centers = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]

        # O(1) loop (9x9) to check by row
        for i in range(len(board)):
            temp = {}
            for j in range(len(board[0])):
                if board[i][j] != "." and board[i][j] in temp:
                    return False
                temp[board[i][j]] = 1

        # O(1) loop (9x9) to check by column
        for i in range(len(board[0])):
            temp = {}
            for j in range(len(board)):
                if board[j][i] != "." and board[j][i] in temp:
                    return False
                temp[board[j][i]] = 1

        # O(1) loop (9x9) to check for boxes
        for i in centers:
            temp = {}
            for j in neighbors:
                if board[i[0] + j[0]][i[1] + j[1]] != "." and board[i[0] + j[0]][i[1] + j[1]] in temp:
                    return False
                temp[board[i[0] + j[0]][i[1] + j[1]]] = 1

        return True
