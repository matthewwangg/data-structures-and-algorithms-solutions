class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def setZero(i, j):
            for k in range(len(matrix)):
                if matrix[k][j] != 0:
                    matrix[k][j] = float('inf')

            for k in range(len(matrix[0])):
                if matrix[i][k] != 0:
                    matrix[i][k] = float('inf')

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    setZero(i, j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0


