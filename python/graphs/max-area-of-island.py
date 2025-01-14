class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        neighbors = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        maxarea = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return 0

            count = 1
            grid[i][j] = 2
            for neighbor in neighbors:
                count += dfs(i + neighbor[0], j + neighbor[1])

            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxarea = max(maxarea, dfs(i, j))

        return maxarea
