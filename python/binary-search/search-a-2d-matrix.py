class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            middle = (left + right) // 2
            if target <= matrix[middle][-1] and target >= matrix[middle][0]:
                row = middle
                left, right = 0, len(matrix[0]) - 1
                while left <= right:
                    middle = (left + right) // 2
                    if target == matrix[row][middle]:
                        return True
                    else:
                        if target < matrix[row][middle]:
                            right = middle - 1
                        else:
                            left = middle + 1

                break
            else:
                if target < matrix[middle][0]:
                    right = middle - 1
                else:
                    left = middle + 1

        return False