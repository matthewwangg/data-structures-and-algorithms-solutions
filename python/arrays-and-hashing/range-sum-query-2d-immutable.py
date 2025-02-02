class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.matrix[i + 1][j + 1] = matrix[i][j]
                self.matrix[i + 1][j + 1] += self.matrix[i + 1][j] + self.matrix[i][j + 1] - self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2 + 1][col2 + 1] + self.matrix[row1][col1] - self.matrix[row2 + 1][col1] - \
            self.matrix[row1][col2 + 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)