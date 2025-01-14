class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
                return

            grid[i][j] = "2"
            for neighbor in neighbors:
                dfs(i + neighbor[0], j + neighbor[1])

            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count