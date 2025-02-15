"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def split(grid, i, j, w):
            def allSame(grid, i, j, w):
                value = grid[i][j]
                for row in range(i, i + w):
                    for col in range(j, j + w):
                        if value != grid[row][col]:
                            return False
                return True

            if allSame(grid, i, j, w):
                return Node(grid[i][j] == 1, True)

            node = Node(False, False)
            node.topLeft = split(grid, i, j, w // 2)
            node.topRight = split(grid, i, j + w // 2, w // 2)
            node.bottomLeft = split(grid, i + w // 2, j, w // 2)
            node.bottomRight = split(grid, i + w // 2, j + w // 2, w // 2)
            return node

        return split(grid, 0, 0, len(grid))
