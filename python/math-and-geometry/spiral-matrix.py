class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        distance, direction = 0, 0
        n = len(matrix) * len(matrix[0])
        elements = []
        i, j = 0, 0
        while n > 0:
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                break
            elements.append(matrix[i][j])
            if direction == 0:
                j += 1
                if j == len(matrix[0])-distance:
                    direction = 1
                    j -= 1
                    i += 1
            elif direction == 1:
                i += 1
                if i == len(matrix)-distance:
                    direction = 2
                    i -= 1
                    j -= 1
            elif direction == 2:
                j -= 1
                if j == distance-1:
                    direction = 3
                    j += 1
                    i -= 1
                    distance += 1
            elif direction == 3:
                i -= 1
                if i == distance-1:
                    i += 1
                    j += 1
                    direction = 0
            n -= 1

        return elements
